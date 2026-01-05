#learning python for script, backend and security

name = input("enter your name: ")
age = int(input("enter your age: "))

print("\n---Python and Cyber Security learning---")

print(f"\nHabari! {name}, Karibu kwenye ulimwengu wa Pyhton na Linux")

if age >= 18:
    print("wewe ni mtu mzima, unaweza kuanza kujifunza advanced cyber security.")
else:
    print("Bado mdogo, lakini python inakufaa pia!")




#simulated security scanner / list ya hudumatunazo taka kuangalia
huduma_za_server = ["Database", "Web Server", "Email Services", "SSH"]

huduma_za_server.append("FTP")

print("\n\n--- Anza Kukagua Usalama Wa Mfumo ---")

for huduma in huduma_za_server:
    print(f"\nInakagua: {huduma}...")
    if huduma == "SSH":
        print(f"WARNING: {huduma} inahitaji password Imara!")
    elif huduma == "FTP":
        print(f"CRITICAL: {huduma} Funga port hii mara moja, Haina usalama!")
    else:
        print(f"SALAMA: {huduma} haina tatizo.")

print("\n--- Ukaguzi umekamilika ---")