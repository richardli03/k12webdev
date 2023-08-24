import csv
import os

VALID_TAGS = ["grade-2-5", "grade-6-8", "grade-9-12",
              "science", "technology", "engineering", "art", "math",
              "prep-1", "prep-1-2", "prep-2-3", "prep-3+"]


def convert_csv(csv_path):
    data_list = []

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["TITLE"].strip()
            tags = row["TAGS"].strip().split(",")
            tags = [tag.lower().strip() for tag in tags]
            description = row["DESCRIPTION"].strip()
            subpage_path = row["PATH TO SUBPAGE"].strip()
            thumbnail_path = row["PATH TO THUMBNAIL"].strip()
            download_path = row["PATH TO DOWNLOAD"].strip()
            data_list.append(
                (title, tags, description, subpage_path, thumbnail_path, download_path))

    return data_list


def translate_tags(tags):
    tag_mapping = {
        "grade-2-5": "2nd-5th grade",
        "grade-6-8": "6th-8th grade",
        "grade-9-12": "9th-12th grade",
        "science": "Science",
        "technology": "Technology",
        "engineering": "Engineering",
        "art": "Art",
        "math": "Math",
        "prep-1": "~1 hour",
        "prep-1-2": "~1-2 hours",
        "prep-2-3": "~2-3 hours",
        "prep-3+": "~3+ hours"
    }

    translated_tags = []
    for tag in tags:
        if tag in tag_mapping:
            translated_tags.append(tag_mapping[tag.lower()])
        else:
            pass
            # print(f"tag {tag} not found in tag_mapping dict")

    return ", ".join(translated_tags)


def generate_workshop(title, tags, description, path_to_subpage, path_to_thumbnail, path_to_download):
    tags_with_spaces = ""
    for tag in tags:
        tags_with_spaces = tags_with_spaces + tag.strip() + " "
    # print(tags)
    # print(translate_tags((tags)))
    read_tags = translate_tags(tags)
    # print(read_tags)
    html_code = f'''
        <div class="workshop-item col-md-4 mb-4 {tags_with_spaces}">
            <div class="">
                <a href="{path_to_subpage}">
                    <div class="img-holder">
                        <img class="img-fluid" src="{path_to_thumbnail}" alt="">
                    </div>
                </a>
                <div class="workshop-caption">
                    <p class="tags">{read_tags}</p>
                    <h4>{title} <a href="{path_to_download}" download>
                            <img id="download" src="assets/download.png"> </a> </h4>
                    <p class="workshop-description">{description}</p>
                </div>
            </div>
        </div>
        '''
    # print(html_code)
    return html_code


# Example usage:
if __name__ == "__main__":
    DATABASE = "workshops - DATA.csv"  # Replace with the path to your CSV file
    result_list = convert_csv(DATABASE)

    # DUMP RESULTS TO OUT.TXT FILE FOR EASIER COPY AND PASTE
    out_file = "out.txt"
    if os.path.exists(out_file):
        os.remove(out_file)

    for result in result_list:
        html_output = generate_workshop(
            result[0], result[1], result[2], result[3], result[4], result[5])
        with open("out.txt", "a") as file:
            file.write(html_output)
