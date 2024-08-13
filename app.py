import streamlit as st 
import preprocessor, helper
import matplotlib.pyplot as plt 
import plotly.graph_objects as go
import seaborn as sns 


st.sidebar.title("WhatsApp Chat Analyzer")


upload_file = st.sidebar.file_uploader("Choose a file")
if upload_file is not None:
    bytes_data = upload_file.getvalue()
    # NOw lets convert from bytes to string
    data = bytes_data.decode("utf-8")
    # st.text(data)
    df = preprocessor.preprocess(data)


    # fetching unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis w.r.t", user_list)
    if st.sidebar.button("Show Analysis"):

        num_msg, words, num_media_msg, num_links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        # STATS
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_msg)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_msg)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        # Monthly Timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)


        # Daily Timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], marker='o', linestyle='-', color='b')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)


        # Week Activity (Days)

        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='red')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        
        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig,ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)


        # Activity Heatmap
        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)

        if not user_heatmap.empty:
            fig, ax = plt.subplots(figsize=(20, 6))
            sns.heatmap(user_heatmap, cmap="YlGnBu", cbar_kws={'label': 'Message Count'}, ax=ax)
            ax.set_title(f"Activity Heatmap for {selected_user}")
            ax.set_xlabel('Period')
            ax.set_ylabel('Day of the Week')
            st.pyplot(fig)
        else:
            st.write("No data available for the selected user.")
            

        # MOST ACTIVE USER IN THE GROUP(this is group level and is not applicable to individual user)
        if selected_user == 'Overall':
            st.title("Most Active User")
            x, new_df = helper.most_active_users(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            
            with col2:
                st.dataframe(new_df)

    # Worldcloud
    st.title("Wordcloud")
    df_wc = helper.create_worcloud(selected_user,df)
    fig,ax = plt.subplots()
    ax.imshow(df_wc)
    st.pyplot(fig)


    # Most common worsd
    most_common_df = helper.most_common_words(selected_user, df)
    fig,ax = plt.subplots()
    ax.barh(most_common_df[0], most_common_df[1]) #barh = horizonatl bar chart
    plt.xticks(rotation='vertical')
    st.title("Most Common Words")
    st.pyplot(fig)


# WILL IMPLELEMENT THIS PART LATER
    # Emojis
    # emoji_df = helper.emoji_analyse(selected_user,df)
    # st.title("Emoji Analysis")

    # col1, col2 = st.columns(2)

    # with col1:
    #     st.dataframe(emoji_df)

    # with col2:
    #     fig = go.Figure(data=[go.Pie(labels=emoji_df[0].head(), values=emoji_df[1].head(), textinfo='label+percent')])
    #     fig.update_traces(textposition='inside', textfont_size=14)
    #     st.plotly_chart(fig)


st.info("For a better view, follow these steps:")
st.text("1. Click the three-line icon on the top right corner.")
st.text("2. Click 'Settings'.")
st.text("3. Select 'Wider View' for better visibility.")
