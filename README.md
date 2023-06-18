
# FoxMental

**FoxMental** is a provisional name for a program designed to monitor psychological health using cognitive-behavioral therapy methods. The program was developed as a diploma project and has now received its first working prototype. Python programming language and the TTKBOOTSTRAP library for building graphical interfaces were used in the development of the program.

## Installation

The repository can be cloned using the standard template. After installation, the GUI needs to be installed using the following command in the terminal:
```python
pip install ttkbootstrap
```

## Usage

### Before using this program, please familiarize yourself with the following rules:
- This application is in the testing and prototyping stage. Surveys undergo verification by specialized professionals in the field of psychology and psychiatry.
- The application does not provide clinical diagnoses.
- Do not consider survey results as final; additional consultation with a specialist is necessary in any case.

## Testing
![Testing](https://i.ibb.co/0Q5TP4n/image.png)

In this tab, you can take tests for the following conditions:
- Seasonal Affective Disorder
- Post-Traumatic Stress Disorder
- Obsessive-Compulsive Disorder
- Self-Esteem Test
- Cognitive Distortions Test
- Depression
- Anxiety Disorder
- General Psychological State Test

Your task is simply to click on the appropriate button, which will open a new window with the test.

## "Situation-Thought-Emotion-Action" Table
![STEА Table](https://i.ibb.co/stvYYrf/image.png)

In this tab, you can fill in the STEA table related to a situation that has occurred with you. The STEA table is a key tool for cognitive-behavioral therapists. Remember to save your entries.

## "Notepad" Table
![Notepad Table](https://i.ibb.co/fC402j1/image.png)

In this tab, there is a simple text widget that allows you to take notes. Remember to save your entries.

## "Instructions" Table
![Instructions Table](https://i.ibb.co/VpvZHzp/FAQ.png)

In this tab, instructions for the user are duplicated, and compliance with these instructions is mandatory for using the program.

## Some Technical Aspects of the Code
### Algorithm for Generating Menu Buttons
First, buttons are generated using a loop. Then, during the test selection, the Text parameter of the button is compared with the test name. If there is a match, the second window is activated.
```python
# Button Buildings Loop
self.r, self.c = 0, 0
for i in range(0, 8):
    button = tkb.Button(self.Frame_For_Buttons bootstyle='info'text=self.variants_list[i], width=30)
    button.config(command=lambda button=button: self Tests_Main_Logic(button)) 
    button.grid(row=self.r, column=self.c, padx=10,pady=10)
        self.r += 1
        if self.r == 4:
            self.c += 1
            self.r = 0

def Tests_Main_Logic(self, button):
    for i, test in enumerate(self.variants_list):
        if self.variants_list[i] == button["text"]:
            test = twf.TestingFrame(self.variants_list[i])
             test.mainloop()
        
```
### Algorithm for Generating Survey
The survey is generated in a new window. The test_db file contains a dictionary consisting of keys representing the survey names and lists associated with those keys. The lists include the actual survey questions. The survey is passed through a loop, which generates the survey.
```python
for test, quastions in tdb.TEST_DATABASE.items():
    if test == self.test_title:
        i = 0
        for quastion in quastions:
        var = tkb.IntVar()
        self.vars.append(var)
        tkb.Checkbutton(self.quastions_frame bootstyle='primary', variable=var,text=quastion, offvalue=0, onvalue=1).grid(row=i, column=1, padx=10, pady=6, sticky="w")
        i += 1
        print(i)
```
### Formatting of Surveys
Here is an example of how the depression survey is formatted in the test_db file.
```python
TEST_DATABASE = {
    "ДЕПРЕСІЯ": [
        "Ви відчуваєте постійний невпорядок",
        "У вас є постійне відчуття сумності",
        "Ви відчуваєте постійну втому та зниження енергії",
        "Ви стали байдужими до раніше цікавої речі",
        "Ви відчуваєте неприємні та дискомфортні фізичні відчуття, такі як біль у м'язах або головні болі",
        "Ви маєте проблеми зі сном, такі як невміння заснути або просинання вночі",
        "Чи знаходите ви задоволення від раніше приємних для вас речей, які робили ви",
        "Ви стали менш активними, ніж зазвичай",
        "Ви маєте проблеми зі здатністю зосереджуватися на роботі чи в навчанні",
        "Ви відчуваєте постійну тривогу або напругу",
        "Ви відчуваєте вину за щось або вважаєте себе непотрібним",
        "Ви відчуваєте про смерть або самогубство"],
```

## Future Plans
### Tkinter + Python ---> Dart + Flutter

Since in 2023, the graphical library Tkinter is already considered outdated, it has been decided to finish the program during the testing period on real rails. After the final release and publication of the program in the Scopus journal, it will be redesigned for mobile platforms.

## Contact

Creator: Kior Alexander Sergeyevich (kiordev), Bachelor of Computer Science and student at the Ukrainian Institute of Applied Psychology and Psychotherapy, "Gestalt Therapy" course.

**Telegram:** [revenant_walker](https://t.me/revenant_walker)  
**Gmail:** kiordev@gmail.com

## Acknowledgments
- **Marchenko Irina Fedorovna**, Dean of the Faculty of Social Sciences and Humanities, for mentoring during the development of the diploma project.
- **Balalaeva Alena Yuryevna**, Dean of the Faculty of Information Technology, for providing favorable conditions for project implementation.
- **Tuzenko Olga Aleksandrovna**, lecturer at the Department of Informatics, for supervision and assistance.
- **Sergienko Anastasia Valentinovna**, Head of the Department of Informatics, for supervision and assistance.
- **Teaching staff of the Ukrainian Institute of Applied Psychology and Psychotherapy** for their assistance and consultation in the field of psychology.
