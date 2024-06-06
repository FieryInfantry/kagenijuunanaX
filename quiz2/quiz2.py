from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.metrics import dp


class StudentFormApp(MDApp):
    def build(self):
        
        return Builder.load_file('quiz2.kv')

    def on_add(self):
        student_no = self.root.ids.student_no.text
        first_name = self.root.ids.first_name.text
        last_name = self.root.ids.last_name.text
        course = self.root.ids.course.text
        year = self.root.ids.year.text
        if (student_no != '' and last_name != ''
            and first_name != '' and course != '' and year != ''):
            print('Student no : '+ str(student_no)
                + ' Name :' + str(last_name)
                + ' ' + str(first_name)
                + ' Course :' + str(course)
                + ' year ' + str(year))
        else:
            toast("Blank entries detected!")
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
