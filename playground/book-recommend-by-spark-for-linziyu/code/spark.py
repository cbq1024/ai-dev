from pathlib2 import Path
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import date_format, split, rank
from pyspark.sql.window import Window

"""
book_id,title,authors,average_rating,isbn,isbn13,language_code,
num_pages,ratings_count,text_reviews_count,publication_date,publisher
"""

book_fields_with_first_authors = "book_id,title,SUBSTRING_INDEX(authors, '/', 1) AS first_author,average_rating,language_code,text_reviews_count,publication_date,publisher"

def average_rating(spark, output_path, count):
    """
     根据 average_rating(该书收到的书面文本评论总数) 统计前 count 本书籍
    :param spark: spark instance
    :param output_path: the dir to output the file
    :param count: top sum
    :return: saved file
    """
    book_list = spark.sql(f"SELECT {book_fields_with_first_authors} FROM books \
                              ORDER BY average_rating DESC")
    output_path = output_path / "average_rating"
    if not output_path.exists():
        book_list.write.csv(str(output_path), mode='overwrite')
    print(f"\t\t\t\t\t |---------------> top_{count}_average_rating <---------------| \t\t\t\t\t")
    book_list.show(n=count, truncate=False)

def num_pages(spark, output_path, count):
    """
     根据 num_pages(主书页数) 统计前 count 本书籍
    :param spark: spark instance
    :param output_path: the dir to output the file
    :param count: top sum
    :return: saved file
    """
    book_list = spark.sql(f"SELECT {book_fields_with_first_authors} FROM books \
                              ORDER BY num_pages DESC")
    output_path = output_path / "num_pages"
    if not output_path.exists():
        book_list.write.csv(str(output_path), mode='overwrite')
    print(f"\t\t\t\t\t |---------------> top_{count}_num_pages <---------------| \t\t\t\t\t")
    book_list.show(n=count, truncate=False)

def ratings_count(spark, output_path, count):
    """
     根据 ratings_count(收到的唯一评分数量) 统计前 count 本书籍
    :param spark: spark instance
    :param output_path: the dir to output the file
    :param count: top sum
    :return: saved file
    """
    book_list = spark.sql(f"SELECT {book_fields_with_first_authors} FROM books \
                              ORDER BY ratings_count DESC")
    output_path = output_path / "ratings_count"
    if not output_path.exists():
        book_list.write.csv(str(output_path), mode='overwrite')
    print(f"\t\t\t\t\t |---------------> top_{count}_ratings_count <---------------| \t\t\t\t\t")
    book_list.show(n=count, truncate=False)

def text_reviews_count(spark, output_path, count):
    """
     根据 text_reviews_count(该书收到的书面文本评论总数) 统计前 count 本书籍
    :param spark: spark instance
    :param output_path: the dir to output the file
    :param count: top sum
    :return: saved file
    """
    book_list = spark.sql(f"SELECT {book_fields_with_first_authors} FROM books \
                          ORDER BY text_reviews_count DESC")
    output_path = output_path / "text_reviews_count"
    if not output_path.exists():
        book_list.write.csv(str(output_path), mode='overwrite')
    print(f"\t\t\t\t\t |---------------> top_{count}_text_reviews_count <---------------| \t\t\t\t\t")
    book_list.show(n=count, truncate=False)

def main():
    # path init
    root_path = Path(__file__).resolve().parents[1]
    data_path = root_path / "data" / "cleaned"
    output_path = root_path / "temp"

    # spark init
    spark = SparkSession.builder.config(conf=SparkConf()).getOrCreate()
    books_df = spark.read.csv(str(data_path / "books-kaggle-mohamadreza-momeni.csv"), header=True, inferSchema=True)
    books_df = books_df.repartition(1)
    books_df.createOrReplaceTempView("books")

    average_rating(spark, output_path, 10)
    num_pages(spark, output_path, 10)
    ratings_count(spark, output_path, 10)
    text_reviews_count(spark, output_path, 10)



if __name__ == '__main__':
    main()
