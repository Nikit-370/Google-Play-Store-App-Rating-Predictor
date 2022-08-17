from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['Name']
        category = request.POST['category']
        size = request.POST['size']
        installs = request.POST['installs']
        type = request.POST['type']
        price = request.POST['price']
        content = request.POST['content']
        year = request.POST['year']
        month = request.POST['month']
        day = request.POST['day']

        if name != "":
            df = pd.DataFrame(columns=['Category', 'Size', 'Installs',
                                       'Type', 'Price',	'Content Rating', 'year', 'month', 'day'])

            df2 = {'Category': int(category), 'Size': float(size), 'Installs': int(installs),
                    'Type': int(type), 'Price': float(price), 'Content Rating': int(content),
                    'year': int(year), 'month': int(month), 'day': int(day)}

            df = df.append(df2, ignore_index=True)
            # load the model from disk
            filename = 'polls/AppsPCA.pickle'
            pca = pickle.load(open(filename, 'rb'))
            data = pca.transform(df)
            filename1 = 'polls/Apps.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))

            res = loaded_model.predict(data)
            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})
