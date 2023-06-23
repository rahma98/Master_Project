def eda(request):
    
    # Specify the path to your CSV file
    csv_path = 'df.csv'

   
    spark = SparkSession.builder.appName("platform").getOrCreate()
    sparkDF =spark.read.csv(csv_path ,header=True,inferSchema=True)
    
    selected_columns = []  # Initialize the variable with an empty list
    
    if request.method == "POST":
        # Get the selected columns from the form data
        selected_columns = request.POST.getlist("columns")

        # Select desired columns from the DataFrame
        data = sparkDF.select(selected_columns)

    # Pass the DataFrame and selected columns to the template context
    context = {
        "data": data.toPandas(),
        "selected_columns": selected_columns if selected_columns else [],
    }

    
    return render(request, 'eda.html',context )
# -*- coding: utf-8 -*-

