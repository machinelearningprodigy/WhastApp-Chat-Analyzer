# 📊 WhatsApp Chat Analyzer

Welcome to the WhatsApp Chat Analyzer! This tool allows you to upload and analyze your WhatsApp chat history, providing insightful statistics and visualizations about your conversations.

Live Demo: [WhatsApp Chat Analyzer](https://whatsapp-chat-analyzer-24.streamlit.app/) 🎉

## 🎯 Features

- **Top Statistics**: Get an overview of the total messages, words, media shared, and links shared in the chat.
- **Monthly Timeline**: Visualize the number of messages exchanged each month.
- **Daily Timeline**: Track daily messaging activity.
- **Activity Map**: Discover the most active days and months in your chat.
- **Weekly Activity Map**: Heatmap showing the messaging activity throughout the week.
- **Most Active Users**: Identify the most active participants in the chat.
- **Wordcloud**: Generate a wordcloud of the most frequently used words in the chat.
- **Most Common Words**: List the most common words used in the chat.
- **Supports 12-Hour Time Format**: Specifically designed to work with WhatsApp chats exported in 12-hour time format.

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- Streamlit
- Required Python packages: `pandas`, `seaborn`, `matplotlib`, `plotly`, `wordcloud`, `emoji`, `urlextract`, `nltk`

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/whatsapp-chat-analyzer.git
    cd whatsapp-chat-analyzer
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

4. **Upload your WhatsApp chat file:**

    - Export your WhatsApp chat from your mobile device.
    - Upload the `.txt` file into the app.

## 🧠 How It Works

1. **Data Preprocessing:**
   - The uploaded chat file is converted from bytes to a string.
   - Dates, times, and messages are extracted using regular expressions.
   - The chat data is then processed to separate user names and messages, which are stored in a pandas DataFrame.

2. **Analysis:**
   - **Top Statistics:** Computes the total number of messages, words, media files, and links shared.
   - **Timelines:** Visualize messaging activity over time using monthly and daily timelines.
   - **Activity Maps:** Understand the most active days of the week and months of the year.
   - **Wordcloud & Common Words:** Generate a wordcloud and identify the most common words used in the chat.
   - **Heatmap:** Displays weekly activity based on the time of day and day of the week.
   - **Most Active Users:** For group chats, identify the most active participants.

3. **Visualization:**
   - Interactive plots and charts are generated using `matplotlib`, `seaborn`, and `plotly`.
   - A wordcloud is created using the `WordCloud` library to highlight frequently used words.

## 📈 Example Outputs

### 🏆 Top Statistics


### 📅 Monthly Timeline

### 🔥 Weekly Activity Map


### 🌟 Wordcloud


## 🤖 Built With

- [Streamlit](https://streamlit.io/) - The fastest way to build and share data apps.
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis.
- [Seaborn](https://seaborn.pydata.org/) - Statistical data visualization.
- [Matplotlib](https://matplotlib.org/) - Plotting and visualization.
- [Plotly](https://plotly.com/) - Interactive graphs and plots.
- [WordCloud](https://github.com/amueller/word_cloud) - A little word cloud generator in Python.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


Happy Analyzing! 🎉
