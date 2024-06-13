
import httpx
import asyncio
import stripe
from pyrogram import filters
from EQUROBOT import app

# Configure Stripe API Key
stripe.api_key = 'your_stripe_api_key_here'

async def check_card_with_gateway(card_number, expiry_date, cvv):
    url = "https://mock-payment-gateway.com/api/check_card"  # Hypothetical URL
    payload = {
        "card_number": card_number,
        "expiry_date": expiry_date,
        "cvv": cvv
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.json()

def check_card_with_stripe(card_number, exp_month, exp_year, cvv):
    try:
        token = stripe.Token.create(
            card={
                "number": card_number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvv,
            },
        )
        return {"status": "passed", "token": token.id}
    except stripe.error.CardError as e:
        return {"status": "declined", "error": str(e)}

@app.on_message(filters.command(["bulkcheckcc"], [".", "", "!", "/"]))
async def bulk_check_cc(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "**Hey, please provide credit card details in the format: /bulkcheckcc card1:expiry1:cvv1, card2:expiry2:cvv2, ...**"
        )
    
    try:
        await message.delete()
    except Exception as e:
        print(f"Error deleting message: {e}")
    
    aux = await message.reply_text("<b>Checking the credit cards, please wait...</b>")
    
    cards_data = message.text.split(None, 1)[1].split(',')
    tasks = []
    
    for card_data in cards_data:
        parts = card_data.strip().split(':')
        if len(parts) != 3:
            return await aux.edit("<b>Oops, buddy, wrong format. Please provide details in the format card:expiry:cvv.</b>")
        
        card_number, expiry_date, cvv = parts
        exp_month, exp_year = expiry_date.split('/')
        if not card_number.isdigit() or len(card_number) < 12 or len(card_number) > 19:
            return await aux.edit(f"<b>Invalid card number: {card_number}. Please provide a valid credit card number.</b>")
        
        # Check with hypothetical gateway
        tasks.append(check_card_with_gateway(card_number, expiry_date, cvv))
        # Check with Stripe
        tasks.append(asyncio.to_thread(check_card_with_stripe, card_number, exp_month, exp_year, cvv))
    
    results = await asyncio.gather(*tasks)
    valid_cards = []
    invalid_cards = []

    for i, result in enumerate(results):
        card_number = cards_data[i // 2].strip().split(':')[0]
        if result['status'] == 'passed':
            valid_cards.append(card_number)
        else:
            invalid_cards.append(card_number)
    
    response_text = "<b>Bulk Credit Card Check Results:</b>\n"
    response_text += f"\n<b>✅ Valid Cards:</b> {', '.join(valid_cards) if valid_cards else 'None'}"
    response_text += f"\n<b>🚫 Invalid Cards:</b> {', '.join(invalid_cards) if invalid_cards else 'None'}"
    
    await aux.edit(response_text)

@app.on_message(filters.command(["checkfilecc"], [".", "", "!", "/"]))
async def check_file_cc(client, message):
    if not message.document:
        return await message.reply_text("Please send a text file containing card details.")
    
    file_path = await client.download_media(message.document)
    
    try:
        with open(file_path, 'r') as file:
            cards_data = file.read().strip().split('\n')
    except Exception as e:
        return await message.reply_text(f"Error reading file: {e}")
    
    aux = await message.reply_text("<b>Checking the credit cards from file, please wait...</b>")
    
    tasks = []
    
    for card_data in cards_data:
        parts = card_data.strip().split(':')
        if len(parts) != 3:
            return await aux.edit("<b>Oops, buddy, wrong format in file. Please provide details in the format card:expiry:cvv.</b>")
        
        card_number, expiry_date, cvv = parts
        exp_month, exp_year = expiry_date.split('/')
        if not card_number.isdigit() or len(card_number) < 12 or len(card_number) > 19:
            return await aux.edit(f"<b>Invalid card number in file: {card_number}. Please provide a valid credit card number.</b>")
        
        # Check with hypothetical gateway
        tasks.append(check_card_with_gateway(card_number, expiry_date, cvv))
        # Check with Stripe
        tasks.append(asyncio.to_thread(check_card_with_stripe, card_number, exp_month, exp_year, cvv))
    
    results = await asyncio.gather(*tasks)
    valid_cards = []
    invalid_cards = []

    for i, result in enumerate(results):
        card_number = cards_data[i // 2].strip().split(':')[0]
        if result['status'] == 'passed':
            valid_cards.append(card_number)
        else:
            invalid_cards.append(card_number)
    
    response_text = "<b>File Credit Card Check Results:</b>\n"
    response_text += f"\n<b>✅ Valid Cards:</b> {', '.join(valid_cards) if valid_cards else 'None'}"
    response_text += f"\n<b>🚫 Invalid Cards:</b> {', '.join(invalid_cards) if invalid_cards else 'None'}"
    
    await aux.edit(response_text)
