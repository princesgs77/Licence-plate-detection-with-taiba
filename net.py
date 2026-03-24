from pyngrok import ngrok

ngrok.set_auth_token("3BNuLTSHvX3WcMMpMSG7OhEmmUV_DuiJg9wiPuQ2sigUHJ4K")

public_url = ngrok.connect(4747)
print("NGROK URL:", public_url)

# 🔥 KEEP PROCESS ALIVE
input("Press Enter to stop ngrok...")