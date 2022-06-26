from utilities import print_message, get_size, order_latte, order_mocha
from classes import Menu

def coffee_bot():
  print('Welcome to the Kafe Lakay!')

  menu_list = {
              'Small':{'Brewed Coffee':1.50, 'Iced Coffee':1.75, 'Mocha':2.00, 'Latte':2.75},
              'Medium':{'Brewed Coffee':2.00, 'Iced Coffee':2.25, 'Mocha':2.50, 'Latte':3.25},
              'Large':{'Brewed Coffee':2.25, 'Iced Coffee':2.50, 'Mocha':2.75, 'Latte':3.75}
              }

  for key in menu_list:
    print('\n' + key)
    print('----------')
    for value in menu_list[key]:
        print(value, ": $", menu_list[key][value])
  
  order_drink = 'y'

  drinks_list = []  

  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks_list.append(drink)

    while True:
      order_drink = input("Would you like to order another drink? (y/n) \n> ")
      if order_drink in ['y', 'n']:
        break
    print('Okay, so I have: ')
    for drink in drinks_list:
      print('-', drink)
  
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))



def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
        if purchased_item in self.items:
            bill += self.items(purchased_item)
    return bill
coffee_bot()



