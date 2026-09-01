import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def main():
    if not os.path.exists("client_secret.json"):
        print("Fout: client_secret.json niet gevonden in de hoofdmap!")
        print("Download je OAuth client ID bestand van Google Cloud Console en zet het hier neer.")
        return

    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token_file:
        token_file.write(creds.to_json())

    print("\nSucces! token.json is gegenereerd.")

if __name__ == "__main__":
    main()
