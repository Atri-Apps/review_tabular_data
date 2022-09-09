from .atri import Atri
from fastapi import Request, Response
from atri_utils import *
import pandas as pd

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    df = pd.read_csv('most_popular_books.csv')
    # df = pd.DataFrame(
    #     {'id': [1, 2], 'col2': [0.5, 0.75]}, index=['a', 'b'])
    at.Table3.custom.cols = [
        {'field':'id', 'headerName':'id'},
        {'field':'Name', 'headerName':'Name', 'width':400},
        {'field':'Author', 'headerName':'Author', 'width':200},
        {'field':'Rating', 'headerName':'Rating'},
        {'field':'Reviews', 'headerName':'Reviews'},
        {'field':'Price', 'headerName':'Price'},
        {'field':'Year', 'headerName':'Year'},
        {'field':'Genre', 'headerName':'Genre'},
    ]
    at.Table3.custom.rows = df.to_dict(orient='records')

    #comment 1
    at.Table6.custom.cols = [
        {'field':'id', 'headerName':'id'},
        {'field':'Name', 'headerName':'Name', 'width':400},
        {'field':'Author', 'headerName':'Author', 'width':200},
        {'field':'Rating', 'headerName':'Rating'},
        {'field':'Reviews', 'headerName':'Reviews'},
        {'field':'Price', 'headerName':'Price'},
        {'field':'Year', 'headerName':'Year'},
        {'field':'Genre', 'headerName':'Genre'},
    ]
    at.Table6.custom.rows = df.head(1).to_dict(orient='records')

    #comment 2
    at.Table7.custom.cols = [
        {'field':'id', 'headerName':'id'},
        {'field':'Name', 'headerName':'Name', 'width':400},
        {'field':'Author', 'headerName':'Author', 'width':400},
        {'field':'Rating', 'headerName':'Rating'},
        {'field':'Reviews', 'headerName':'Reviews'},
        {'field':'Price', 'headerName':'Price'},
        {'field':'Year', 'headerName':'Year'},
        {'field':'Genre', 'headerName':'Genre'},
    ]
    at.Table7.custom.rows = df.tail(2).to_dict(orient='records')

    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    pass

def write_table(df, cols):
    at.Table.custom.rows = df.to_dict(orient='records')

    