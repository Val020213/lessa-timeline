import streamlit as st
from streamlit_timeline import timeline
import streamlit as st
import json


def main():

    def upload_timeline_title():
        try:
            st.session_state["timeline"] = {
                "title": {
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

        st.button(
            label="Submit",
            use_container_width=True,
            help="Submit the form to see the timeline.",
            on_click=upload_timeline_title,
        )

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

        st.button(
            label="Agregar evento",
            use_container_width=True,
            help="Submit the form to see the timeline.",
            on_click=upload_event,
        )

        st.download_button(
            label="Descargar JSON",
            use_container_width=True,
            file_name="timeline.json",
            help="Descarga el JSON de la timeline",
            data=json.dumps(st.session_state.timeline),
        )

    else:
        st.warning("Please submit the timeline form to see the timeline.")

        def upload_file():
            if st.session_state.file:
                try:
                    file_content = st.session_state.file.read()
                    st.session_state.timeline = json.loads(file_content)
                except Exception as e:
                    st.error(f"Error: {e}, please upload a valid JSON file.")

        st.file_uploader(
            label="Upload JSON file",
            type=["json"],
            help="Upload a CSV file with the timeline data.",
            key="file",
            on_change=upload_file,
        )


if __name__ == "__main__":
    st.set_page_config(page_title="Lessa Story Timeline", layout="wide", page_icon="📅")

    main()
