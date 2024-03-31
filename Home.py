'''import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/title_image.png")

with col2:
    st.title("Harmony")
    st.info("""
    Introducing MindEase, the ultimate mobile app dedicated to promoting mental well-being and fostering mindfulness.
    With personalized tools ranging from mood tracking and guided meditations to stress reduction exercises, MindEase empowers individuals to proactively manage stress, anxiety, and depression. 
    Connect with a supportive community, access teletherapy services, and utilize evidence-based cognitive behavioral therapy tools to challenge negative thought patterns and build resilience. 
    Receive daily reminders and challenges, track your progress, and cultivate positive habits for a healthier, happier life. 
    Join MindEase today and embark on a journey towards greater peace, resilience, and well-being.
    """)

st.title(" ")
st.title(" ")
st.title(" ")
st.title(" ")
st.markdown("<h1 style='text-align: center;'>How are you feeling today?</h1>",
            unsafe_allow_html=True)
st.title(" ")

col3, col4, col5, col6, col7, empty_col, col8 = st.columns([1, 1, 1, 1, 1, 0.2, 1.5])

with col3:
    st.image("emote_images/crying.png")
    st.markdown("<h4><div style='text-align: center;'>Depressed</div></h4>",
                unsafe_allow_html=True)

with col4:
    st.image("emote_images/unhappy.png")
    st.markdown("<h4><div style='text-align: center;'>Sad</div></h4>",
                unsafe_allow_html=True)

with col5:
    st.image("emote_images/neutral.png")
    st.markdown("<h4><div style='text-align: center;'>Okay</div></h4>",
                unsafe_allow_html=True)

with col6:
    st.image("emote_images/happy.png")
    st.markdown("<h4><div style='text-align: center;'>Happy</div></h4>",
                unsafe_allow_html=True)

with col7:
    st.image("emote_images/laughing.png")
    st.markdown("<h4><div style='text-align: center;'>Overjoyed</div></h4>",
                unsafe_allow_html=True)

with col8:
    st.markdown("<h5><div style='text-align: center;'>Select the emoji that best describes how you feel</div></h5>",
                unsafe_allow_html=True)
    selected_emoji = st.selectbox(" ",
                                 ["Depressed", "Sad", "Okay", "Happy", "Overjoyed"],
                                 key="selected_emoji")
st.title(" ")
st.title(" ")

match selected_emoji:
    case "Depressed":
        col9, col10 = st.columns(2)

        with col9:
            st.image("images/depressed.png")
        with col10:
            st.title("Feeling depressed?")
            st.info("""
            We understand navigating feelings of depression can be incredibly challenging.
            The weight of these emotions may feel overwhelming, but we are here to provide help and support.
            Harmony is committed towards individuals like you, who are struggling with mental health issues.
            It's important to acknowledge that your feelings are valuable to us.
            Whether you are looking for resources, information or simply a listening ear, we are here to help.
            """)

        st.header("Here are some things you can do to feel better:- ")

        col11, col12 = st.columns(2)

        with col11:
            st.markdown("<h4><div style='text-align: center;'>Self-Care</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
            You can engage in various self-care activities to feel better. 
            You can engage in activities such as taking a warm bath, going out in nature, writing, painting etc.
            Sleep deprivation can worsen symptoms of depression, so prioritize getting proper sleep and maintain a healthy sleep schedule
            Incorporate physical activity in your routine.
            Exercises release natural mood boosters called endorphines, and help with feelings of stress and anxiety.
            A short run or a gentle yoga session can be more than enough.
            At the same time, pay attention to your nutrition and maintain a balanced diet.           
            """)

        with col12:
            st.markdown("<h4><div style='text-align: center;'>Meditation</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
            Meditation is a great tool for dealing with stress and anxiety. It can help to calm your mind down.
            Find a quiet place to sit or lie down, and close your eyes to start meditating.
            If you don't know where to start, simply focus on your breath.
            When inhaling and exhaling, non-verbally count "one" or "two" respectively to yourself.
            If you find yourself distracted, simply start over from beginning.
            Some people might find simply counting numbers to be better, or more challenging than this technique.
            Remember, the best meditation technique is the one that suits you.
            """)

        col13, col14 = st.columns(2)

        with col13:
            st.markdown("<h4><div style='text-align: center;'>Take things one at a time</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
            Remember to take things one at a time. 
            You should prioritize your mental health.
            Taking breaks is an okay thing to do.
            Break your tasks into smaller and more manageable segments, and focus on achieving one goal at a time.
            Keep celebrating your achievements along the way, no matter how small.
            This will help you stay motivated and stress free.
            """)

        with col14:
            st.markdown("<h4><div style='text-align: center;'>Seek support or professional help</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
            If you are dealing with stress or depression, don't hesitate to reach out for support to someone you trust,
            whether it is a friend or a family member. If necessary, reach out to a professional,
            such as a therapist or psychiatrist.
            Sharing your feelings with someone can help with the feeling of isolation that often accompanies anxiety or depression.            
            """)


    case "Sad":
        col15, col16 = st.columns(2)

        with col15:
            st.image("images/sad.png")

        with col16:
            st.title("Are you feeling sad?")
            st.info("""
            Everyone feels sad from time to time.
            It is a natural and common emotion.
            While this is normal, it is important to address your feelings properly and nurture your well being.
            Harmony is committed to dealing with your mental health and feelings of such.
            """)

        st.header("Here are some suggestions you can follow:- ")

        col17, col18 = st.columns(2)

        with col17:
            st.markdown("<h4><div style='text-align: center;'>Practice gratitude</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
                    Gratitude is a rare but great quality to have.
                    Cultivate a mindset of gratitude by focusing on the positive aspects of your life, even during difficult times. 
                    Take time each day to reflect and show gratitude towards on things you're grateful for, 
                    whether it's small moments of joy, relationships, or personal accomplishments. 
                    Practicing gratitude can shift your perspective and increase feelings of contentment and happiness.         
                    """)

        with col18:
            st.markdown("<h4><div style='text-align: center;'>Limit exposure to social media and news</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
                    Most people spend a considerable amount of time on social media.
                    Therefore, what content you consume can have a significant influence on your mental health and feelings.
                    Be mindful of the content you consume, especially on social media and news platforms. 
                    Limit exposure to negative or triggering content that may exacerbate feelings of sadness. 
                    Instead, focus on sources of positivity and inspiration that uplift and motivate you.
                    """)

        col19, col20 = st.columns(2)

        with col19:
            st.markdown("<h4><div style='text-align: center;'>Engage in meaningful activities</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
                     Find activities that bring meaning and purpose. 
                     Whether it's volunteering, spending time with loved ones, 
                     or pursuing personal goals, engaging in meaningful activities can help you find fulfillment and connection, 
                     even when you are feeling bad.
                    """)

        with col20:
            st.markdown("<h4><div style='text-align: center;'>Express yourself</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
                     Find healthy ways to express your emotions and release pent-up feelings. 
                     This could involve talking to a trusted friend or family member, 
                     journaling your thoughts and feelings, or engaging in creative activities like art or music. 
                     Expressing yourself can help you gain clarity about your emotions.           
                    """)


    case "Okay":
        col21, col22 = st.columns(2)

        with col21:
            st.image("images/okay.png")
        with col22:
            st.title("Thank you for sharing your feelings!")
            st.info("""
                        We are glad that you have decided to share how you feel. 
                        While you are feeling okay, consider how you can nuture yourself and focus on your well being.
                        Engage in relaxing activities today. Reach out to a friend, go out for a walk.
                        Remember, even in moments of balance, your mental health matters. 
                        Explore the resources and support available to you within the app to continue nurturing your emotional well-being. 
                        """)


    case "Happy":
        col22, col23 = st.columns(2)

        with col22:
            st.image("images/happy_image.png")
        with col23:
            st.title("Fantastic")
            st.info("""
            It's wonderful to hear that you're feeling happy today!
            Embrace and celebrate this positive mood by spreading joy and positivity wherever you go. 
            Take a moment to reflect on what's bringing you happiness right now and express gratitude for those moments. 
            Whether it's the sunshine on your face, 
            a kind word from a friend, or a personal achievement, cherish these moments of happiness. 
            Remember, happiness is contagious! 
            Share your joy with others, spread kindness, and brighten someone else's day. 
            Explore the resources and activities within the app to continue nurturing your happiness and well-being. Keep smiling! 
            """)


    case "Overjoyed":
        col24, col25 = st.columns(2)

        with col24:
            st.image("images/overjoyed.png")
        with col25:
            st.title("Congrats!")
            st.info("""
            Woo-hoo! Congratulations on feeling extremely overjoyed! 
            This level of happiness is truly something to celebrate! 
            Take a moment to bask in the glow of your joy and revel in the abundance of positive energy surrounding you. 
            Allow yourself to fully embrace and savor this moment of pure bliss. 
            Reflect on what's contributing to your overwhelming happiness and express gratitude for these incredible blessings. 
            Share your contagious enthusiasm with others, spread smiles, and uplift those around you. 
            Keep shining brightly and continue to radiate positivity wherever you go!
            """)
'''
import streamlit as st

# Add CSS for background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff; /* Light Blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/title_image.png")

with col2:
    st.title("Harmony")
    st.info("""
    Introducing MindEase, the ultimate mobile app dedicated to promoting mental well-being and fostering mindfulness.
    With personalized tools ranging from mood tracking and guided meditations to stress reduction exercises, MindEase empowers individuals to proactively manage stress, anxiety, and depression. 
    Connect with a supportive community, access teletherapy services, and utilize evidence-based cognitive behavioral therapy tools to challenge negative thought patterns and build resilience. 
    Receive daily reminders and challenges, track your progress, and cultivate positive habits for a healthier, happier life. 
    Join MindEase today and embark on a journey towards greater peace, resilience, and well-being.
    """)

st.title(" ")
st.title(" ")
st.title(" ")
st.title(" ")
st.markdown("<h1 style='text-align: center;'>How are you feeling today?</h1>",
            unsafe_allow_html=True)
st.title(" ")

col3, col4, col5, col6, col7, empty_col, col8 = st.columns([1, 1, 1, 1, 1, 0.2, 1.5])

with col3:
    st.image("emote_images/crying.png")
    st.markdown("<h4><div style='text-align: center;'>Depressed</div></h4>",
                unsafe_allow_html=True)

with col4:
    st.image("emote_images/unhappy.png")
    st.markdown("<h4><div style='text-align: center;'>Sad</div></h4>",
                unsafe_allow_html=True)

with col5:
    st.image("emote_images/neutral.png")
    st.markdown("<h4><div style='text-align: center;'>Okay</div></h4>",
                unsafe_allow_html=True)

with col6:
    st.image("emote_images/happy.png")
    st.markdown("<h4><div style='text-align: center;'>Happy</div></h4>",
                unsafe_allow_html=True)

with col7:
    st.image("emote_images/laughing.png")
    st.markdown("<h4><div style='text-align: center;'>Overjoyed</div></h4>",
                unsafe_allow_html=True)

with col8:
    st.markdown("<h5><div style='text-align: center;'>Select the emoji that best describes how you feel</div></h5>",
                unsafe_allow_html=True)
    selected_emoji = st.selectbox(" ",
                                 ["Depressed", "Sad", "Okay", "Happy", "Overjoyed"],
                                 key="selected_emoji")
st.title(" ")
st.title(" ")

match selected_emoji:
    case "Depressed":
        col9, col10 = st.columns(2)

        with col9:
            st.image("images/depressed.png")
        with col10:
            st.title("Feeling depressed?")
            st.info("""
            We understand navigating feelings of depression can be incredibly challenging.
            The weight of these emotions may feel overwhelming, but we are here to provide help and support.
            Harmony is committed towards individuals like you, who are struggling with mental health issues.
            It's important to acknowledge that your feelings are valuable to us.
            Whether you are looking for resources, information or simply a listening ear, we are here to help.
            """)

        st.header("Here are some things you can do to feel better:- ")

        col11, col12 = st.columns(2)

        with col11:
            st.markdown("<h4><div style='text-align: center;'>Self-Care</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
            You can engage in various self-care activities to feel better. 
            You can engage in activities such as taking a warm bath, going out in nature, writing, painting etc.
            Sleep deprivation can worsen symptoms of depression, so prioritize getting proper sleep and maintain a healthy sleep schedule
            Incorporate physical activity in your routine.
            Exercises release natural mood boosters called endorphins, and help with feelings of stress and anxiety.
            A short run or a gentle yoga session can be more than enough.
            At the same time, pay attention to your nutrition and maintain a balanced diet.           
            """)

        with col12:
            st.markdown("<h4><div style='text-align: center;'>Meditation</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
            Meditation is a great tool for dealing with stress and anxiety. It can help to calm your mind down.
            Find a quiet place to sit or lie down, and close your eyes to start meditating.
            If you don't know where to start, simply focus on your breath.
            When inhaling and exhaling, non-verbally count "one" or "two" respectively to yourself.
            If you find yourself distracted, simply start over from the beginning.
            Some people might find simply counting numbers to be better, or more challenging than this technique.
            Remember, the best meditation technique is the one that suits you.
            """)

        col13, col14 = st.columns(2)

        with col13:
            st.markdown("<h4><div style='text-align: center;'>Take things one at a time</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
            Remember to take things one at a time. 
            You should prioritize your mental health.
            Taking breaks is an okay thing to do.
            Break your tasks into smaller and more manageable segments, and focus on achieving one goal at a time.
            Keep celebrating your achievements along the way, no matter how small.
            This will help you stay motivated and stress-free.
            """)

        with col14:
            st.markdown("<h4><div style='text-align: center;'>Seek support or professional help</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
            If you are dealing with stress or depression, don't hesitate to reach out for support to someone you trust,
            whether it is a friend or a family member. If necessary, reach out to a professional,
            such as a therapist or psychiatrist.
            Sharing your feelings with someone can help with the feeling of isolation that often accompanies anxiety or depression.            
            """)


    case "Sad":
        col15, col16 = st.columns(2)

        with col15:
            st.image("images/sad.png")

        with col16:
            st.title("Are you feeling sad?")
            st.info("""
            Everyone feels sad from time to time.
            It is a natural and common emotion.
            While this is normal, it is important to address your feelings properly and nurture your well being.
            Harmony is committed to dealing with your mental health and feelings of such.
            """)

        st.header("Here are some suggestions you can follow:- ")

        col17, col18 = st.columns(2)

        with col17:
            st.markdown("<h4><div style='text-align: center;'>Practice gratitude</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
                    Gratitude is a rare but great quality to have.
                    Cultivate a mindset of gratitude by focusing on the positive aspects of your life, even during difficult times. 
                    Take time each day to reflect and show gratitude towards on things you're grateful for, 
                    whether it's small moments of joy, relationships, or personal accomplishments. 
                    Practicing gratitude can shift your perspective and increase feelings of contentment and happiness.         
                    """)

        with col18:
            st.markdown("<h4><div style='text-align: center;'>Limit exposure to social media and news</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
                    Most people spend a considerable amount of time on social media.
                    Therefore, what content you consume can have a significant influence on your mental health and feelings.
                    Be mindful of the content you consume, especially on social media and news platforms. 
                    Limit exposure to negative or triggering content that may exacerbate feelings of sadness. 
                    Instead, focus on sources of positivity and inspiration that uplift and motivate you.
                    """)

        col19, col20 = st.columns(2)

        with col19:
            st.markdown("<h4><div style='text-align: center;'>Engage in meaningful activities</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
                     Find activities that bring meaning and purpose. 
                     Whether it's volunteering, spending time with loved ones, 
                     or pursuing personal goals, engaging in meaningful activities can help you find fulfillment and connection, 
                     even when you are feeling bad.
                    """)

        with col20:
            st.markdown("<h4><div style='text-align: center;'>Express yourself</div></h4>",
                        unsafe_allow_html=True)
            st.info("""
                     Find healthy ways to express your emotions and release pent-up feelings. 
                     This could involve talking to a trusted friend or family member, 
                     journaling your thoughts and feelings, or engaging in creative activities like art or music. 
                     Expressing yourself can help you gain clarity about your emotions.           
                    """)


    case "Okay":
        col21, col22 = st.columns(2)

        with col21:
            st.image("images/okay.png")
        with col22:
            st.title("Thank you for sharing your feelings!")
            st.info("""
                        We are glad that you have decided to share how you feel. 
                        While you are feeling okay, consider how you can nuture yourself and focus on your well being.
                        Engage in relaxing activities today. Reach out to a friend, go out for a walk.
                        Remember, even in moments of balance, your mental health matters. 
                        Explore the resources and support available to you within the app to continue nurturing your emotional well-being. 
                        """)


    case "Happy":
        col22, col23 = st.columns(2)

        with col22:
            st.image("images/happy_image.png")
        with col23:
            st.title("Fantastic")
            st.info("""
            It's wonderful to hear that you're feeling happy today!
            Embrace and celebrate this positive mood by spreading joy and positivity wherever you go. 
            Take a moment to reflect on what's bringing you happiness right now and express gratitude for those moments. 
            Whether it's the sunshine on your face, 
            a kind word from a friend, or a personal achievement, cherish these moments of happiness. 
            Remember, happiness is contagious! 
            Share your joy with others, spread kindness, and brighten someone else's day. 
            Explore the resources and activities within the app to continue nurturing your happiness and well-being. Keep smiling! 
            """)


    case "Overjoyed":
        col24, col25 = st.columns(2)

        with col24:
            st.image("images/overjoyed.png")
        with col25:
            st.title("Congrats!")
            st.info("""
            Woo-hoo! Congratulations on feeling extremely overjoyed! 
            This level of happiness is truly something to celebrate! 
            Take a moment to bask in the glow of your joy and revel in the abundance of positive energy surrounding you. 
            Allow yourself to fully embrace and savor this moment of pure bliss. 
            Reflect on what's contributing to your overwhelming happiness and express gratitude for these incredible blessings. 
            Share your contagious enthusiasm with others, spread smiles, and uplift those around you. 
            Keep shining brightly and continue to radiate positivity wherever you go!
            """)
