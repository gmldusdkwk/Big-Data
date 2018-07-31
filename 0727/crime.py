import pandas as pd


def pandas_index2():
    crime = pd.read_hdf('/Users/limheeyeon/PycharmProjects/0727/crime.h5')
    crime2 = crime[['OFFENSE_TYPE_ID', 'GEO_LON', 'GEO_LAT']].head(100)
    x = crime2.to_records(index=False)
    marker = []
    for i in x:
        p = {'icon':'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png', 'lat': i[2], 'lng': i[1], 'infobox': "<b>%s</b>" % i[0]}
        marker.append(p)
    return marker
