from render import Render
from subprocess import check_output as runmyscript

class Myfunc():
    pic=False
    js=False
    css=False
    mymusic=False
    json=False
    figure=Render("hi") 
    upload=False
    redirect=False
    myfile=False
    mydata=False
    myargs=False
    someparam={}
    my_params=figure.get_my_params()
    myattributes=[]
    figure=False
    
    myprmogram=False
    run=False
    path=False
    runthisprogram=False
    def set_someparam(self,x,y):
        self.someparam[x]=y
    def get_someparams(self):
        return self.someparam
    def get_someparam(self,x):
        return self.someparam[x]
    def set_myargs(self,x):
        self.myargs=x
    def get_myargs(self):
        return self.myargs
    def set_json(self,x):
        self.json=x
        if self.json:
          self.figure.set_body("")
    def get_json(self):
        return self.json
    def set_css(self,x):
        self.css=x
        if self.css:
          self.figure.set_body("")
    def get_css(self):
        return self.css
    def set_redirect(self,x):
        self.redirect=x
    def get_redirect(self):
        return self.redirect
    def set_mydata(self,x):
        self.mydata=x
    def get_mydata(self):
        return self.mydata
    def set_runthisprogram(self,run=False):
        self.runthisprogram=run
    def get_runthisprogram(self):
        return self.runthisprogram
    def runprogram(self):
        if self.myfile and self.myfile.endswith(".sh"):
            return "sh"
        elif self.myfile and self.myfile.endswith(".py"):
            return "python3"
        elif self.get_progtam():
            return self.get_program()
        else:
            return None

    def run(self):
        arr=[]
        if self.get_runthisprogram():
            if self.get_myargs():
                arr=self.get_myargs()
                script=runmyscript(arr)
                self.figure.my_params["myoutput"]= script
            elif self.runprogram():
                arr.append(self.runprogram())
                if self.myfile:
                    arr.append(self.get_path()+"/"+self.myfile)
                script=runmyscript(arr)
                self.figure.my_params["myoutput"]= script
    def set_file(self,x):
        self.myfile=x
    def get_program(self,x):
        self.myprogram=x
    def set_program(self,x):
        self.myprogram=x
    def get_path(self):
        return self.path
    def set_path(self,x):
        self.path=x
    def get_figure(self):
        return self.figure
    def get_pic(self):
        return self.pic
    def get_music(self):
        return self.mymusic
    def get_js(self):
        return self.js
    def set_attributes(self,name):
        self.myattributes=name
    def get_attributes(self):
        return self.myattributes
    def set_uploads(self,name):
        self.upload=name
    def get_uploads(self):
        return self.upload
    def get_upload(self):
        return self.upload
    def get_html(self):
        return self.get_figure().render_figure().encode()
    def file(self,params):
        print("frgthjk")
    def work(self,params):
        loc={"self":self, "params": params}
        exec("myvar=self.{myfunc}(params)".format(myfunc=self.path), globals(), loc)
        return loc["myvar"]

