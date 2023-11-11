adminid = "61646d696e"
adminpwd = "70617373776f7264"
#data = {"Site Name": ["Year Created", "Creator", "Location", "Nearest Airport", "Distance from Airport", "State", "Description"}
from difflib import get_close_matches
from getpass import getpass
from pprint import pprint
from os import system

data = {
	"Taj Mahal": ["1632", "Mughal Emperor Shah Jahan", "Agra, Uttar Pradesh", "Indira Gandhi International Airport", "10 km", "Uttar Pradesh", "An eternal symbol of love, the Taj Mahal is an iconic white marble mausoleum that stands on the banks of the Yamuna River."],
	"Qutub Minar": ["12th century", "Qutb-ud-din Aibak", "Delhi", "Indira Gandhi International Airport", "5 km", "Delhi", "The Qutub Minar is a towering masterpiece of Mughal architecture and is recognized as the world's tallest brick minaret."],
	"Jaipur City, Rajasthan": ["18th century", "Sawai Jai Singh II", "Jaipur, Rajasthan", "Jaipur International Airport", "15 km", "Rajasthan", "Known as the Pink City, Jaipur is a historic city renowned for its majestic palaces, vibrant bazaars, and cultural richness."],
	"Ajanta Caves": ["2nd and 1st centuries BCE", "Various rulers", "Maharashtra", "Aurangabad Airport", "8 km", "Maharashtra", "The Ajanta Caves are a UNESCO World Heritage Site featuring ancient Buddhist cave temples adorned with exquisite paintings and sculptures."],
	"Ellora Caves": ["6th-9th centuries", "Various rulers", "Maharashtra", "Aurangabad Airport", "12 km", "Maharashtra", "A marvel of rock-cut architecture, the Ellora Caves showcase a harmonious blend of Hindu, Jain, and Buddhist temples."],
	"Sundarbans National Park": ["Not applicable", "Not applicable", "West Bengal", "Netaji Subhas Chandra Bose International Airport", "20 km", "West Bengal", "The Sundarbans is the largest mangrove forest in the world, a UNESCO site, and a critical habitat for the Bengal tiger."],
	"Hampi": ["14th-16th centuries", "Various rulers", "Karnataka", "Hubli Airport", "25 km", "Karnataka", "Hampi is a captivating ruin city that was once the capital of the Vijayanagara Empire, boasting splendid temples and ancient monuments."],
	"Agra Fort": ["16th century", "Akbar the Great", "Agra, Uttar Pradesh", "Indira Gandhi International Airport", "8 km", "Uttar Pradesh", "Agra Fort is a historical fortress with Mughal architectural grandeur and served as the main residence of the emperors."],
	"Khajuraho Group of Monuments": ["10th-12th centuries", "Various rulers", "Madhya Pradesh", "Khajuraho Airport", "5 km", "Madhya Pradesh", "Renowned for its intricate erotic sculptures, the Khajuraho Group of Monuments is a testament to medieval Indian art and architecture."],
	"Sun Temple": ["13th century", "Narasimhadeva I", "Odisha", "Biju Patnaik International Airport", "15 km", "Odisha", "The Sun Temple in Konark is a UNESCO World Heritage Site, dedicated to the Sun God, and is famous for its colossal chariot-shaped architecture."],
	"Rani-ki-Vav": ["11th century", "Rani Udayamati", "Gujarat", "Sardar Vallabhbhai Patel International Airport", "10 km", "Gujarat", "Rani-ki-Vav is an intricately designed stepwell in Patan, representing a stunning blend of art and utility."],
	"Elephanta Caves": ["5th-6th centuries", "Various rulers", "Maharashtra", "Chhatrapati Shivaji Maharaj International Airport", "7 km", "Maharashtra", "The Elephanta Caves on Elephanta Island are home to ancient rock-cut sculptures and cave temples dedicated to Hindu deities."],
	"Chhatrapati Shivaji Terminus": ["19th century", "Frederick William Stevens", "Mumbai, Maharashtra", "Chhatrapati Shivaji Maharaj International Airport", "2 km", "Maharashtra", "Formerly known as Victoria Terminus, it's a UNESCO World Heritage Site and a masterpiece of Victorian-Gothic architecture."],
	"Mountain Railways of India": ["19th-20th centuries", "British colonial authorities", "Varies by location", "Various states", "Not applicable", "The Mountain Railways of India include three historic railway lines that traverse picturesque landscapes, offering a nostalgic journey."],
	"Great Living Chola Temples": ["11th-12th centuries", "Various rulers", "Tamil Nadu", "Chennai International Airport", "12 km", "Tamil Nadu", "A group of ancient temples built during the Chola dynasty, showcasing remarkable Dravidian architecture."],
	"Group of Monuments at Mahabalipuram": ["7th-8th centuries", "Pallava dynasty", "Tamil Nadu", "Chennai International Airport", "15 km", "Tamil Nadu", "Mahabalipuram is known for its intricately carved temples and rock-cut sculptures, reflecting Pallava artistry."],
	"Rock Shelters of Bhimbetka": ["Mesolithic period", "Ancient inhabitants", "Madhya Pradesh", "Raja Bhoj Airport", "10 km", "Madhya Pradesh", "The Rock Shelters of Bhimbetka are an archaeological site with ancient cave paintings, providing a glimpse into prehistoric human life."],
	"Champaner-Pavagadh Archaeological Park": ["8th-14th centuries", "Various rulers", "Gujarat", "Sardar Vallabhbhai Patel International Airport", "5 km", "Gujarat", "Champaner-Pavagadh is an archaeological park with a mix of religious, military, and residential structures showcasing diverse architectural styles."],
	"Jantar Mantar": ["18th century", "Sawai Jai Singh II", "Jaipur, Rajasthan", "Jaipur International Airport", "10 km", "Rajasthan", "Jantar Mantar is an astronomical observatory with a collection of architectural astronomical instruments built during the early 18th century."],
	"Western Ghats": ["Not applicable", "Not applicable", "Various states", "Varies by location", "Not applicable", "The Western Ghats, a UNESCO World Heritage Site, are a mountain range known for their biodiversity, unique ecosystems, and cultural significance."],
	"Keoladeo National Park": ["Not applicable", "Not applicable", "Rajasthan", "Jaipur International Airport", "20 km", "Rajasthan", "Keoladeo National Park, also known as Bharatpur Bird Sanctuary, is a haven for migratory birds and a UNESCO site."],
	"Hill Forts of Rajasthan": ["Varies by fort", "Various rulers", "Rajasthan", "Maharana Pratap Airport", "85 km", "Rajasthan", "A collection of forts representing Rajput military architecture, including Amber Fort, Chittorgarh Fort, Mehrangarh Fort, Ranthambore Fort, Gagron Fort, and Bundi Fort."],
	"Amber Fort": ["16th century", "Raja Man Singh I", "Jaipur, Rajasthan", "Jaipur International Airport", "15 km", "Rajasthan", "Amber Fort is a majestic fort known for its stunning architecture, intricate mirror work, and panoramic views of the surrounding hills."],
	"Chittorgarh Fort": ["7th century", "Various rulers", "Udaipur, Rajasthan", "Maharana Pratap Airport", "60 km", "Rajasthan", "Chittorgarh Fort is the largest fort in India and has historical significance as the site of several battles and acts of heroic sacrifice."],
	"Mehrangarh Fort": ["1459", "Rao Jodha", "Jodhpur, Rajasthan", "Jodhpur Airport", "10 km", "Rajasthan", "Mehrangarh Fort is an impressive hill fort perched above the city of Jodhpur, housing museums and offering breathtaking views of the Blue City."],
	"Ranthambore Fort": ["10th century", "Various rulers", "Sawai Madhopur, Rajasthan", "Jaipur International Airport", "150 km", "Rajasthan", "Ranthambore Fort is located within Ranthambore National Park and is known for its historical ruins and wildlife sightings."],
	"Gagron Fort": ["8th century", "Rulers of Jhalawar", "Jhalawar, Rajasthan", "Jaipur International Airport", "100 km", "Rajasthan", "Gagron Fort is a unique fort surrounded by water on three sides and is recognized for its strategic location and architectural brilliance."],
	"Bundi Fort": ["14th century", "Rao Deva Hada", "Bundi, Rajasthan", "Jaipur International Airport", "210 km", "Rajasthan", "Bundi Fort is a historical fort in the town of Bundi, known for its impressive architecture, including step wells and painted murals."],
}

def ifExists(site:str):
	if site in data.keys():
		return site
	else:
		guess = get_close_matches(site, data.keys())
		if guess!=[] and input(f"Site not found\nDid you mean: {guess[0]}?\n").lower()[0] == 'y':
			return guess[0]
		else:
			print("It seems that we do not have that site in our registry")
			exit(1)

#login
user = input("Enter username: ")
#login to admin console
if user.encode('utf-8').hex() == adminid:

	for i in range(1, 4):
		if getpass("Enter Password: ").encode('utf-8').hex() == adminpwd:
			print("Logged in as Admin")
			input("Press Enter to continue\n")
			system('cls')
			break

		else:
			print(f"Incorrect Password\n{3-i} attempts remaining")
			if 3-i >0:
				input("Press Enter to try again\n")
				system('cls')

			else:
				print("Too many incorrect attempts\nExiting...")
				exit(2)
	#Main Admin Menu
	print("Admin Console:\n\
	1. Add Site\n\
	2. Modify Site\n\
	3. Delete Site\n\
	4. Change admin password\n\
	5. Exit")
	
	match input("Enter Option: "):

		#Add Site
		case "1":
			name = input("Name of site: ")
			data[name] = [input("Year of Establishment: "), input("Creator: "), input("Location: "), input("Closest Airport: "), input("Distance from airport: "), input("State: "), input("Description: ")]
			print(f"List Updated:")
			pprint(data)

		#Modify Site
		case "2":
			name = input("Name of site: ")
			name = ifExists(name)
			
			match input(f"What do you want to edit:\n\
	1. Year of establishment(Current: {data[name][0]})\n\
	2. Creator(Current: {data[name][1]})\n\
	3. Location of site(Current: {data[name][2]})\n\
	4. Nearest Airport(Current: {data[name][3]})\n\
	5. Description\n"):
				
				case "1":
					system('cls')
					data[name] = [input("Updated Year of Establishment"), data[name][1], data[name][2], data[name][3], data[name][4], data[name][5], data[name][6]]
			
				case "2":
					system('cls')
					data[name] = [data[name][0], input("Updated Creator: "), data[name][2], data[name][3], data[name][4], data[name][5], data[name][6]]
				
				case "3":
					system('cls')
					state = input("Updated State: ")
					data[name] = [data[name][0], data[name][1], f"{input("Updated City/District Name: ")}, {state}", data[name][3], data[name][4], state, data[name][6]]
				
				case "4":
					system('cls')	
					data[name] = [data[name][0], data[name][1], data[name][2], input("Updated Closest Airport: "), input("Distance from Updated Airport"), data[name][5], data[name][6]]
				
				case "5":
					system('cls')
					data[name] = [data[name][0], data[name][1], data[name][2], data[name][3], data[name][4], data[name][5], input("Updated description: ")]
			
			print(f"List Updated:")
			pprint(data)
		#Delete Site
		
		case "3":
			system('cls')
			name = input("Name of site: ")
			name = ifExists(name)
		
			if input(f"Are you sure you want to delete {name}: ").lower()[0] == 'y':
				del data[name]
				print("List Updated")
				pprint(data)
		#Change Password
		
		case "4":
			system('cls')
			if getpass("Enter old password: ").encode('utf-8').hex() == adminpwd:
				pwd = getpass("Enter new password: ")
		
				if pwd == getpass("Enter new password again:"):
					with open('main.py') as f:
					
						lines = f.readlines()
						lines[1] = f'adminpwd = "{str(pwd.encode('utf-8').hex())}"\n'
						f.close()
		
					with open('main.py', 'w') as f:
						f.writelines(lines)
						f.close()
					print("Password Changed Succesfully")
					system('py main.py')
		
				else:
					print("Password does not match\nExiting...")
					exit(2)
		
			else:
				print("Incorrect Password\nExiting...")
		
		case "5":
			print("Exiting...")
			exit(0)
else:
	#Main User Menu
	while True:
		system('cls')
		match input(f"Welcome {user}, what do you want to do today?\n\
	1. Display all sites\n\
	2. Get Information on a specific site\n\
	3. Search for site by State\n\
	4. Display Raw Data of all sites\n\
	5. Exit\n"):
		
			#Display All Sites
			case "1":
				system('cls')
				for i in range(len(list(data))):
					print(f"{i+1}. {list(data)[i]}")
		
			#Info of Specific Site
			case "2":
				system('cls')
				name = input("Enter Site Name: ")
				name = ifExists(name)
				print(f"{name.upper()}\n\
	Year Established: {data[name][0]}\n\
	Created By: {data[name][1]}\n\
	Located at: {data[name][2]}\n\
	Nearest Airport is {data[name][3]} and it is {data[name][4]}(s) away\n\
	\n{data[name][6]}")
		
			#Search by State
			case "3":
				system('cls')
				state = input("Enter State: ")
				for i in range(len(list(data))):
					if data[list(data)[i]][5].lower() == state.lower():	
						print(f"{list(data)[i]}")
			
			#Raw Data
			case "4":
				system('cls')
				pprint(data)
		
			#Exit
			case "5":
				break
			case _:
				print("Choice not available...")
		
		if input("\nDo you want to get more information: ").lower()[0] == 'y':
			pass
		else:
			break
	
	print("Thank you for using our database\nGoodbye...")
	exit(0)