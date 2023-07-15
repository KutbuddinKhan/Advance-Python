class Page:
    def __init__(self, heading, body):
        self.heading = heading
        self.body = body
    
    def create_page(self):
        html = f"<h1>{self.heading}</h1>\n<p>{self.body}</p>"
        return html
    
class Contact(Page):
    def __init__(self, heading, body, emai_id):
        # self.heading = heading
        # self.body = body
        # Avoding above repeatation code use super function
        super().__init__(heading, body)
        self.email_id = emai_id

    def create_contact_button(self):
        return f"<button>{self.email_id}, contact now! </button>"


contact_page = Contact("Contact us", "Please give us your feedback", "Kkhan@gmail.com")
print(contact_page.create_page())
print(contact_page.email_id)
print(contact_page.create_contact_button())

# check is instance of the class or not
print(isinstance(contact_page, Contact))
print(isinstance(contact_page, Page))