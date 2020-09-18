import argparse
from os import path
from converter import Converter
from converter.factories.AnnotationFactory import Factory as A_Factory
from converter.factories.GroundtruthFactory import Factory as G_Factory
from converter.factories.XmlFactory import Factory as Xml_Factory
from converter.factories.TFRecordFactory import Factory as Tf_Factory

def usage():
    return """
        python main.py pascal_to_groundtruth --s3_path s3://somepath/ --pascal_label_path local/path --output example.manifest
        python main.py pascal_to_tfrecords --pascal_label_path local/path --output example.records
    """

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instagram Crawler", usage=usage())
    parser.add_argument(
        "mode", help="options: [pascal_to_groundtruth, pascal_to_tfrecords]"
    )
    parser.add_argument("--s3_path", help="S3 path needed for Groundtruth, should be where you images are stored")
    parser.add_argument("--pascal_label_path", help="Directory to pascal label peth")
    parser.add_argument("--output", help="Output path")

    args = parser.parse_args()
    Converter().setLabelmap()

    if args.mode == "pascal_to_groundtruth":
        if not args.s3_path or not args.pascal_label_path:
            raise Exception("s3_path and pascal_label_path required for execution") 
        
        annotationFactory = A_Factory()
        groundtruthFactory = G_Factory(args.s3_path)

        pascal_annotation = annotationFactory.generate_from_directory(path=path.join(args.pascal_label_path))
        groundtruth_annotation = groundtruthFactory.generate_groundtruths(pascal_annotation)

        groundtruthFactory.output_file(groundtruth=groundtruth_annotation, output_path=args.output)
    elif args.mode == "pascal_to_tfrecords":
        if args.s3_path or args.pascal_label_path:
            raise Exception("pascal_label_path required for execution") 
        xmlFactory = Xml_Factory()
        tfFactory = Tf_Factory()

        xml_df = xmlFactory.generate_xml_from_pascal(path=path.join(args.pascal_label_path))
        # output csv file
        xmlFactory.output_file(xml_df)

        tfFactory.output_file(image_dir=path.join(args.pascal_label_path), csv_input='output.csv', output=args.output)
    else:
        usage()
