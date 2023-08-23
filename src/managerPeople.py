class ManagerPeople:

    def __init__(self):
        self.people = []
    
    def insert_person(self, person):
        self.people.append(person)

    def consult_person(self, name):
        for person in self.people:
            if person.name == name:
                return person
        return None  # If person isn't foundered
    
    def update_person(self, name, new_data):
        name = self.consult_person(name)
        if name:
            name.name = new_data['name']
            name.age = new_data['age']
            name.mail = new_data['mail']
            name.height = new_data['height']
            name.is_student = new_data['is_student']
            return True

        return False  # If person isn't foundered
    
    def delete_person(self, name):
        person = self.consult_person(name)
        if person:
            self.people.remove(person)
            return True
