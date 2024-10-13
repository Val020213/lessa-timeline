import base64
import streamlit as st
from streamlit_timeline import timeline
import streamlit as st
import pandas as pd
from io import StringIO
from PIL import Image


def main():

    def upload_timeline_title():
        try:
            st.session_state["timeline"] = {
                "title": {
                    "media": {
                        "url": (
                            f"data:image/jpeg;base64,{base64.b64encode(st.session_state.timeline_title_image.read()).decode('utf-8')}"
                            if st.session_state.timeline_title_image
                            else ""
                        ),
                        "caption": st.session_state.timeline_title_image_caption,
                    },
                    "text": {
                        "headline": st.session_state.timeline_title,
                        "text": st.session_state.timeline_title_description,
                    },
                },
                "events": [],
            }
        except Exception as e:
            st.error(f"Error: {e}, please fill the form correctly.")

    if not st.session_state.get("timeline"):

        st.text_input(
            "Titulo de tu Timeline *",
            key="timeline_title",
            value="Mi Timeline",
            help="",
        )

        st.text_area(
            "Descripción",
            key="timeline_title_description",
            help="Escribe una descripción de tu timeline",
            value="",
        )

        st.text_input(
            "Caption de la imagen",
            key="timeline_title_image_caption",
            value="",
            help="Caption de la imagen",
        )

        uploaded_file = st.file_uploader(
            "Subir imagen",
            type=["png", "jpg", "jpeg"],
            key="timeline_title_image",
            help="Sube una imagen para tu timeline",
        )
        with st.expander("Preview"):
            if uploaded_file is not None:

                try:
                    image = Image.open(uploaded_file)
                    st.image(
                        image,
                        caption="Uploaded Image.",
                        use_column_width=True,
                    )
                except Exception as _:
                    st.write("The uploaded file is not an image.")

        submitted = st.button(
            label="Submit",
            use_container_width=True,
            help="Submit the form to see the timeline.",
            on_click=upload_timeline_title,
        )

        if submitted:

            st.session_state["timeline"] = {
                "title": st.session_state.timeline_title,
                "image": (
                    base64.b64encode(
                        st.session_state.timeline_title_image.read()
                    ).decode("utf-8")
                    if st.session_state.timeline_title_image
                    else ""
                ),
                "description": st.session_state.timeline_title_description,
            }

    if "timeline" in st.session_state:
        timeline_data = {
            "title": st.session_state.timeline["title"],
            "events": st.session_state.timeline["events"],
        }
        timeline(data=timeline_data)

        def upload_event():
            if "events" not in st.session_state.timeline:
                st.session_state.timeline["events"] = []
            try:
                st.session_state.timeline["events"].append(
                    {
                        "media": {
                            "url": "https://tse3.mm.bing.net/th?id=OIP.SMAmS1MxCpssY-raDGzy1wHaE7&pid=Api&P=0&h=220",
                            "caption": st.session_state.event_image_caption,
                        },
                        "start_date": {
                            "year": st.session_state.event_date.year,
                            "month": st.session_state.event_date.month,
                            "day": st.session_state.event_date.day,
                            "hour": st.session_state.event_time.hour,
                            "minute": st.session_state.event_time.minute,
                        },
                        "end_date": {
                            "year": st.session_state.event_end_date.year,
                            "month": st.session_state.event_end_date.month,
                            "day": st.session_state.event_end_date.day,
                            "hour": st.session_state.event_end_time.hour,
                            "minute": st.session_state.event_end_time.minute,
                        },
                        "text": {
                            "headline": st.session_state.event_headline.strip(),
                            "text": st.session_state.event_text.strip(),
                        },
                    }
                )
            except Exception as e:
                st.error(f"Error: {e}, please fill the form correctly.")

        st.container(height=64, border=False)

        event_cols = st.columns(2)
        with event_cols[0]:
            st.text_input(
                "Titulo del evento *",
                key="event_headline",
                value="Mi evento",
                help="",
            )

            st.text_area(
                "Descripción",
                key="event_text",
                help="Escribe una descripción de tu evento",
                value="",
            )

        with event_cols[1]:
            datetime_cols = st.columns(2)
            with datetime_cols[0]:

                st.date_input(
                    "Fecha de inicio *",
                    key="event_date",
                    help="Fecha de inicio del evento",
                )
                st.time_input(
                    "Hora de inicio",
                    key="event_time",
                    help="Hora de inicio del evento",
                )

            with datetime_cols[1]:
                st.date_input(
                    "Fecha de fin",
                    key="event_end_date",
                    help="Fecha de fin del evento",
                )
                st.time_input(
                    "Hora de fin",
                    key="event_end_time",
                    help="Hora de fin del evento",
                )

        st.text_input(
            "Caption de la imagen",
            key="event_image_caption",
            value="",
            help="Caption de la imagen",
        )

        uploaded_file = st.file_uploader(
            "Subir imagen",
            type=["png", "jpg", "jpeg"],
            key="event_image",
            help="Sube una imagen para tu evento",
        )
        with st.expander("Preview"):
            if uploaded_file is not None:

                try:
                    image = Image.open(uploaded_file)
                    st.image(
                        image,
                        caption="Uploaded Image.",
                        use_column_width=True,
                    )
                except Exception as _:
                    st.write("The uploaded file is not an image.")

        submitted = st.button(
            label="Agregar evento",
            use_container_width=True,
            help="Submit the form to see the timeline.",
            on_click=upload_event,
        )

    else:
        st.warning("Please submit the timeline form to see the timeline.")


if __name__ == "__main__":
    st.set_page_config(page_title="Lessa Story Timeline", layout="wide")

    main()

# {
#  "title": {
#             "media": {
#                 "url": "",
#                 "caption": " <a target=\"_blank\" href=''>credits</a>",
#                 "credit": "",
#             },
#             "text": {
#                 "headline": "Welcome to<br>Streamlit Timeline",
#                 "text": "<p>A Streamlit Timeline component by integrating TimelineJS from Knightlab</p>",
#             },
#         },
#         "events": [
#             {
#                 "media": {
#                     "url": "https://vimeo.com/143407878",
#                     "caption": "How to Use TimelineJS (<a target=\"_blank\" href='https://timeline.knightlab.com/'>credits</a>)",
#                 },
#                 "start_date": {"year": "2016", "month": "1"},
#                 "text": {
#                     "headline": "TimelineJS<br>Easy-to-make, beautiful timelines.",
#                     "text": "<p>TimelineJS is a populair tool from Knightlab. It has been used by more than 250,000 people to tell stories seen hundreds of millions of times, and is available in more than sixty languages. </p>",
#                 },
#             },
#             {
#                 "media": {
#                     "url": "https://www.youtube.com/watch?v=CmSKVW1v0xM",
#                     "caption": "Streamlit Components (<a target=\"_blank\" href='https://streamlit.io/'>credits</a>)",
#                 },
#                 "start_date": {"year": "2020", "month": "7", "day": "13"},
#                 "text": {
#                     "headline": "Streamlit Components<br>version 0.63.0",
#                     "text": "Streamlit lets you turn data scripts into sharable web apps in minutes, not weeks. It's all Python, open-source, and free! And once you've created an app you can use our free sharing platform to deploy, manage, and share your app with the world.",
#                 },
#             },
#             {
#                 "media": {
#                     "url": "https://github.com/innerdoc/streamlit-timeline/raw/main/component-logo.png",
#                     "caption": "github/innerdoc (<a target=\"_blank\" href='https://www.github.com/innerdoc/'>credits</a>)",
#                 },
#                 "start_date": {"year": "2021", "month": "2"},
#                 "text": {
#                     "headline": "Streamlit TimelineJS component",
#                     "text": "Started with a demo on https://www.innerdoc.com/nlp-timeline/ . <br>Then made a <a href='https://github.com/innerdoc/streamlit-timeline'>Streamlit component</a> of it. <br>Then made a <a href='https://pypi.org/project/streamlit-timeline/'>PyPi package</a> for it.",
#                 },
#             },
#         ],
#     }
