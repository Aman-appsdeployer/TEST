from flask import Flask, render_template
import psutil 
 

app = Flask(__name__)

def get_drive_space():
    drives = []
    for partition in psutil.disk_partitions():
        drive = {
            'device': partition.device,
            'mountpoint': partition.mountpoint,
            'fstype': partition.fstype
        }
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            drive['total'] = usage.total
            drive['used'] = usage.used
            drive['free'] = usage.free
            drive['percent'] = usage.percent
        except PermissionError:
            continue
        drives.append(drive)
    return drives

@app.route('/')
def index():
    drives = get_drive_space()
    return render_template('index.html', drives=drives)

if __name__ == "__main__":
    app.run(debug=True)
