from stock_trend.pipeline.extract import Extract
from stock_trend.pipeline.transform import Transform
from stock_trend.pipeline.load import Load


def StartPipeline():
    
    YG_df, trend_df = Extract()
    joined_df = Transform(YG_df, trend_df)
    Load(joined_df)
