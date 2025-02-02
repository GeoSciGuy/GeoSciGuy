# Import things
import requests
import os


# helper functions
def current_ndic_pdf_dl():
    try:
        # Create a response object
        txt_loc = 'C:\Dev_Source\github_repos\GeoSciGuy\learning\dl'
        txt_fn = 'current_ndic.pdf'
        text_file = os.path.join(txt_loc,txt_fn)
        print(text_file)

        # res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
        res = requests.get('https://www.dmr.nd.gov/oilgas/daily/2023/dr020323.pdf')
        res.raise_for_status() # this will make the program stop if the above res failes
        playfile = open(text_file,  'wb')
        for chunk in res.iter_content(1000000):
            playfile.write(chunk)
        playfile.close
    except:
        pass


def main():
    try:
        # Put helper functions here:
        current_ndic_pdf_dl()
    except:
        pass

main()

