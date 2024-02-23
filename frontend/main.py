


import streamlit as st
from send_request import get_video_recommendations



def main():
    st.title('Tezda Video Recommendations')
    
    user_id = st.text_input('Enter User ID:')
    
    if st.button('Get Recommendations'):
        if user_id:
            response = get_video_recommendations(user_id)
            recommendations = response['s3_url']
            if recommendations:
                for video_url in recommendations:
                    st.video(video_url)
            else:
                st.error('Failed to retrieve recommendations. Please try again.')
        else:
            st.warning('Please enter a User ID.')


if __name__ == "__main__":
    main()
