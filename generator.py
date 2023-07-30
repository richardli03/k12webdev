import csv


def convert_csv(csv_path):
    data_list = []

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["TITLE"].strip()
            tags = row["TAGS"].strip().split(",")
            description = row["DESCRIPTION"].strip()
            data_list.append((title, tags, description))

    return data_list


def generate_workshop(title, description, tags, path_to_subpage, path_to_thumbnail):
    tags_with_spaces = ""
    for tag in tags:
        tags_with_spaces = tags_with_spaces + tag.strip() + " "
    html_code = f'''
        <div class="workshop-item col-md-4 mb-4 {tags_with_spaces}">
            <div class="">
                <a href="{path_to_subpage}">
                    <div class="img-holder">
                        <img class="img-fluid" src="{path_to_thumbnail}" alt="">
                    </div>
                </a>
                <div class="workshop-caption">
                    <p class="tags">{tags}</p>
                    <h4>{title}</h4>
                    <p class="created-by">{description}</p>
                </div>
            </div>
        </div>
        '''
    return html_code


# Example usage:
if __name__ == "__main__":
    DATABASE = "workshops.csv"  # Replace with the path to your CSV file
    result_list = convert_csv(DATABASE)

    for result in result_list:
        html_output = generate_workshop(result[0], result[2], result[1])
        print(html_output)
