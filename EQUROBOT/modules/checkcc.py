import httpx
from pyrogram import filters
from EQUROBOT import app

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

@app.on_message(filters.command(["checkcc"], [".", "", "!", "/"]))
async def check_cc(client, message):
    if len(message.command) < 4:
        return await message.reply_text(
            "**Hey, please provide a card number, expiry date, and CVV in the format: /checkcc 1234567812345670 12/24 123**"
        )
    
    try:
        await message.delete()
    except Exception as e:
        print(f"Error deleting message: {e}")
    
    aux = await message.reply_text("<b>Checking the credit card, please wait...</b>")
    
    parts = message.text.split()
    card_number = parts[1]
    expiry_date = parts[2]
    cvv = parts[3]
    
    if not card_number.isdigit() or len(card_number) < 12 or len(card_number) > 19:
        return await aux.edit("<b>Oops, buddy, wrong format. Please provide a valid credit card number.</b>")
    
    try:
        result = await check_card_with_gateway(card_number, expiry_date, cvv)
        if result['status'] == 'passed':
            await aux.edit("<b>✅ This credit card passed through the gateway.</b>")
        else:
            await aux.edit("<b>🚫 This credit card was declined by the gateway.</b>")
    except Exception as e:
        print(f"Error checking card: {e}")
        return await aux.edit("**🚫 Error checking card. Please try again later.**")

