from flask import Flask, render_template, url_for

app = Flask(__name__)

data = open(r'C:\Arther\code\python\Notebook\dataset\pokemon.csv').readlines()
pokeNames = []
pokeDit = {}
typCount = {}
for infos in data[1:]:
    infos = infos.split(',')
    pokeNames.append(infos[0])
    if infos[1][:-1] in pokeDit:
        pokeDit[infos[1][:-1]].append(infos[0])
        typCount[infos[1][:-1]] += 1
    else:
        pokeDit[infos[1][:-1]] = [infos[0]]
        typCount[infos[1][:-1]] = 1



@app.route("/")
def home():
    raw_html = """
        <h1>Welcome to the Pokémon App</h1>
        <ul>
            <li><a href="/getcount">Get Pokémon Count</a></li>
            <li><a href="/getDistinctTypes/">Types</a></li>
            <li><a href="/getPokemonByTypeCount/">Types Count</a></li>
        </ul>
"""
    return raw_html


@app.route("/getcount")
def getCount():
    cnt = len(pokeNames)
    return "There are total "+str(cnt)+" Pokemons!"


@app.route("/getPokemonByType/<pType>")
def getByType(pType):
    if pType in pokeDit:
        return pokeDit[pType]
    else:
        return "Invalid Input Type..."

@app.route("/getDistinctTypes/")
def sortByType():      
    return list(pokeDit.keys())

@app.route("/getPokemonByTypeCount/")
def countByType():       
    return typCount


app.run(debug=True)