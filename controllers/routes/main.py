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

    at.Table3.custom.rows, at.Table3.custom.cols = write_table(df, id_col='index',
                                                            col_styles={'Name': {'width':400}, 
                                                            'Author': {'width':200}})

    #comment 1
    at.Table6.custom.rows, at.Table6.custom.cols = write_table(df.head(1), id_col='index',
                                                            col_styles={'Name': {'width':400}, 
                                                            'Author': {'width':200}})
    
    #comment 2
    at.Table7.custom.rows, at.Table7.custom.cols = write_table(df.tail(2), id_col='index',
                                                            col_styles={'Name': {'width':400}, 
                                                            'Author': {'width':200}})

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