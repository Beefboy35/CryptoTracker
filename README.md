               Cryptocurrency tracker
Интерфейс который использует внешнее API из <em>CoinMarketCap</em>
для получения данных.

<em>Как запустить:</em>
<ol>
<li>Регистрируемся на <b>CoinMarketCap</b> и получаем свой API KEY</li>
<li>Создаем файл <b>.env</b> куда вставляем его в формате API_KEY=ваш ключ, также в <b>.env</b> вставляем
API_URL="https://pro-api.coinmarketcap.com"</li>
<li>Запускаем файл <b>main.py</b> и переходим по url: 
<em>http://localhost:7321</em></li>
<li>Доступна две функции <ol>
  <li>Список всех доступных активов (доступен по маршруту <b>/list</b>)</li>
    <li>Расширенная информация по конкретному активу(по маршруту <b>/curr/{id}</b>, где id- идентификатор конкретного актива).
Id можно посмотреть по роуту /list
    </li>
</ol>
</li>
</ol>