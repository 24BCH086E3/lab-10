name = input("Name: ")
phone = input("Phone: ")
email = input("Email: ")

with open("contact.vcf", "w") as file:
    file.write("BEGIN:VCARD\n")
    file.write("VERSION:3.0\n")
    file.write(f"N:{name}\n")
    file.write(f"TEL:{phone}\n")
    file.write(f"EMAIL:{email}\n")
    file.write("END:VCARD\n")
print("vCard saved as contact.vcf")
