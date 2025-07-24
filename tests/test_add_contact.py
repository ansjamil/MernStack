import os
import time

from pages.contact_list_page import ContactListPage
from pages.edit_contact_page import EditContactPage
from pages.home_page import HomePage
from pages.add_contact_page import AddContactPage
from utils.csv_reader import read_contacts_from_csv


def test_add_contact(driver):
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'contacts.csv')
    contacts = read_contacts_from_csv(csv_path)

    # Add the first contact
    contact = contacts[0]
    home = HomePage(driver)
    home.click_add_contact()

    add_page = AddContactPage(driver)
    # add_page.add_contact("cuved", "cuved@gmail.com")
    add_page.add_contact(contact["name"], contact["email"])

    # add_page.click_back_button()
    time.sleep(5)
    list_page = ContactListPage(driver)
    # list_page.search_contact("cuved")
    list_page.search_contact(contact["name"])

    time.sleep(5)



    result_text = list_page.get_result_text()
    # assert "cuved@gmail.com" in result_text
    assert contact["email"] in list_page.get_result_text()

    list_page.click_edit_icon()
    time.sleep(2)

    # Step to update the contact
    edit_page = EditContactPage(driver)
    updated = contacts[1]
    # edit_page.update_contact("DEV", "DEV@gmail.com")  # <--- Updated data
    edit_page.update_contact(updated["name"], updated["email"])

    time.sleep(5)


    # Verify updated contact appears
    # list_page.search_contact("DEV@gmail.com")
    list_page.search_contact(updated["email"])

    time.sleep(2)

    result_text = list_page.get_result_text()
    # assert "DEV@gmail.com" in result_text
    assert updated["email"] in list_page.get_result_text()

