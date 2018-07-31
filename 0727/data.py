def plotdata():
    import seaborn as sns
    from bokeh.plotting import figure
    from bokeh.embed import components
    data = sns.load_dataset('tips')
    data2 = data.groupby(['smoker']).mean().tip
    p = figure(x_range=['YES', 'NO'], plot_width=800, plot_height=800)  # 절대크기만 가능
    p.vbar(['YES', 'NO'], top=data2, width=0.5, fill_color=['red', 'blue'])
    p.y_range.start = 2
    p.y_range.end = 3.5
    return components(p)