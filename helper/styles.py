# styles.py
def custom_css():
    return """
        <style>
        .title {
            font-size: 50px;
            font-weight: bold;
            background: -webkit-linear-gradient(270deg, #CB0000FF, #FF3737FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Custom radio button styles */
        div.stRadio > label {
            font-size: 16px;
            font-weight: bold;
            color: #333;
        }

        .stButton > button {

            color: white;
            border-radius: 12px;
            font-size: 18px;
            font-weight: bold;
            padding: 5px 10px;
            border: none;
            width: 120px;
            transition: 0.3s ease;
        }
        div.stButton > button:first-child:hover {
            background: linear-gradient(to right, #ff5f6d, #ff758c);
            transform: scale(1.05);
        }
    </style>
    """
