from db_helpers import *

#**** eVERYTHING bELOW mIGHT hAVE tO gO tO a nEW pAGE. iN mARKS eXAMPLE hE mODIFIES tHE cODE wITH iNSERTS aND uPDATES aND dELETES


# gO tHROUGH aND cHANGE tHE pASSWORDS aND uSER nAMES tHAT aRE hARD cODED aND uSE ?S 
# cAN sEARCCH uP hOW tO mAKE nAMES nOT hARD cODED. tHIS iS wHERE wE aCCESS tHE db

# boolean called correct
correct = True
while correct:
  username = input("Enter your username: ")
  if username == "p1":
    # tHAT dIDNT wORK sO dELETE tHE .lower iF i cANT fIX iT
    password = input("Enter your password: ")
    if password != '1234':
      print("error, your credentials are incorrect")
    elif password == '1234':
      print('Here are your options: ')
      print('1. Post an exploit')
      print('2. Get all of your exploits')
      print('3. See everyone else\'s exploit')
      print('4. Exit the application')
      # Then the user is redirected to the next screen
      # sTUCK iN a lOOP, nEED tO bREAK iT
      user_choice = input('choose from the above: ')
      # below I will have to add more than print. That is just a placeholder for now. Look at returns instead of prints to retunr values
      if user_choice == '1':
        print('you chose 1')
        run_query("INSERT INTO exploits (content, user_id) VALUES (?,?)", ["join db_helpers and app test"]) 
        # doesnt work but something like this
        # make a post
      elif user_choice == '2':
        print('you chose 2')
        hacker = run_query("SELECT * FROM hackers WHERE id=?",[1]) 
        # this doesnt work either but I think im onto something
      elif user_choice == '3':
        print('you chose 3')
        # hacker = run_query("SELECT * FROM hackers WHERE id!=?",[1]) this doesnt work either but I think im onto something. also notice !=? instead of =?. I'm not sure if that will work, so think of it as sudo code for now
      elif user_choice == '4':
        print('you chose 4')
      else:
        print('error')
        
    
      
      
    else:
      print('error, something went wrong')






































