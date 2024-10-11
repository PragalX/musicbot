import logging
import speedtest
import matplotlib.pyplot as plt
from io import BytesIO
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def speedtest_command(update: Update, context: CallbackContext) -> None:
    logging.info("Speedtest command triggered.")
    # Rest of the code...

    # Your speedtest logic here
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    st.get_best_server()

    download_speed = st.results.download / 1_000_000  # Convert to Mbps
    upload_speed = st.results.upload / 1_000_000      # Convert to Mbps

    # Create a plot
    speeds = [download_speed, upload_speed]
    labels = ['Download Speed', 'Upload Speed']

    fig, ax = plt.subplots()
    ax.bar(labels, speeds, color=['blue', 'orange'])
    ax.set_ylim(0, max(speeds) * 1.2)
    ax.set_ylabel('Speed (Mbps)')
    ax.set_title('Internet Speed Test Results')

    # Save the plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    # Send the image
    update.message.reply_photo(photo=buf)
