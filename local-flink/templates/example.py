import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions([
    "--runner=FlinkRunner",
    "--flink_master=localhost:8081",
    "--environment_type=LOOPBACK"
])
with beam.Pipeline(options) as p:
    print('Write your Beam code below, and it will run on Flink locally.')