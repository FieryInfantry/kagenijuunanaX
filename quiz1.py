from kivy.lang import Builder
from kivymd.app import MDApp

class StudentFormApp(MDApp):
    def build(self):
        # Load the KV file
        return Builder.load_file('quiz.kv')
    
    def on_add(self):
        student_no = self.root.ids.student_no.text
        first_name = self.root.ids.first_name.text
        last_name = self.root.ids.last_name.text
        course = self.root.ids.course.text
        year = self.root.ids.year.text
        # Add your logic here to handle the Add action
        print(f"Add: {student_no}, {first_name}, {last_name}, {course}, {year}")

    def on_edit(self):
        student_no = self.root.ids.student_no.text
        first_name = self.root.ids.first_name.text
        last_name = self.root.ids.last_name.text
        course = self.root.ids.course.text
        year = self.root.ids.year.text
        # Add your logic here to handle the Edit action
        print(f"Edit: {student_no}, {first_name}, {last_name}, {course}, {year}")

    def on_del(self):
        student_no = self.root.ids.student_no.text
        first_name = self.root.ids.first_name.text
        last_name = self.root.ids.last_name.text
        course = self.root.ids.course.text
        year = self.root.ids.year.text
        # Add your logic here to handle the Delete action
        print(f"Delete: {student_no}, {first_name}, {last_name}, {course}, {year}")

if __name__ == '__main__':
    StudentFormApp().run()
