from random import choice

students = ["Punit", "Graham", "Alex", "Karen", "Van",
 "Falwinder", "Gurpreet", "Jasper", "Lyle", 
 "Nega", "Amandeep", "Pawandeep", "Daman", 
 "Pruthviraj", "Beau", "Thilini", "Jashandeep", 
 "Ritesh", "Sahilpreet", "Onkar", "Sourav",
 "Harkamalpreet", "Talwinder"]

print(f"""Dear \033[91m{choice(students)}\033[0m, 
      
We are happy to invite you to our Student Work Exhibition,
happening on \033[91mThursday, 21 September 2023\033[0m,
at the Whitecliffe campus (67 Symonds Street, Auckland)
from \033[91m10:00 AM to 1:00 PM\033[0m.
      
Join us in celebrating the remarkable achievements of our students
and the outstanding work they've accomplished this term.
      
We look forward to seeing you at the exhibition!
      
Best regards,
Ying, Marina, Rashid, John, Pinal""")
