from nltk.sentiment import SentimentIntensityAnalyzer

class MyAlgorithm(QCAlgorithm)

    def Initialize(self)
        self.SetStartDate(2012, 11, 1)
        self.SetEndDate(2017, 1, 1)
        self.SetCash(100000)
        
        self.tsla = self.AddEquity(TSLA, Resolution.Minute).Symbol
        self.musk = self.AddData(MuskTweet, MUSKTWT, Resolution.Minute).Symbol
        
        self.Schedule.On(self.DateRules.EveryDay(self.tsla),
                 self.TimeRules.BeforeMarketClose(self.tsla, 15),      
                 self.exitPosition)

    def OnData(self, data)
        if self.musk in data
            score = data[self.musk].Value
            
            if score  0.5
                self.SetHoldings(self.tsla, 1)
            elif score  -0.5
                self.SetHoldings(self.tsla, -1)

    def exitPosition(self)
        self.Liquidate()


class MuskTweet(PythonData)

    sia = SentimentIntensityAnalyzer()

    def GetSource(self, config, date, isLive)
        source = httpswww.dropbox.comsm5njh7o8x6edzpgMuskProccessedTweet.csvdl=1
        return SubscriptionDataSource(source, SubscriptionTransportMedium.RemoteFile);

    def Reader(self, config, line, date, isLive)
        if not (line.strip() and line[0].isdigit())
            return None
        
        data = line.split(',')
        tweet = MuskTweet()
        
        try
            tweet.Symbol = config.Symbol
            tweet.Time = datetime.strptime(data[0], '%Y-%m-%d %H%M%S') + timedelta(minutes=1)
            content = data[1].lower()
            
            if tsla in content or tesla in content
                tweet.Value = self.sia.polarity_scores(content)[compound]
            else
                tweet.Value = 0
            
        except ValueError
            return None
        
        return tweet