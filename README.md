# top20cities
chart reprs largest cities
Надо взять файл с данными zips.json (http://media.mongodb.org/zips.json)
- загрузить его в mongodb;
- потом поднять flask, соединиться с mongodb;
- вытащить коллекцию, выделить топ-20 городов по количеству населения;
- и передать эти данные на фронт-енд;
- на фронт-енде надо эти данные принять с помощью d3 (или nvd3) ;
- и построить простой график рейтинга городов по убыванию населения.

Data pipeline:
data.json -> (import) -> mongodb
mongodb -> (flask) -> HTTP
HTTP -> (d3.js) -> chart
