from pprint import pprint
from ast import literal_eval as eval


def convert_str_list_to_list(raw_tags: str) -> list:
    """Convert a string meant to represent a list into a list

    :param raw_tags: _description_
    :type raw_tags: str
    :return: _description_
    :rtype: list
    """

    tag_list = eval(raw_tags)
    assert isinstance(tag_list, list)
    return tag_list


def grab_metadata(metadata: list[str], workshop_dictionary: dict) -> dict:
    """Grab all of the metadata to put into a dictionary

    :param markdown: _description_
    :type markdown: list[str]
    """

    for line in metadata:
        split_line = line.split(":")
        if len(split_line) != 2:
            continue
        if (
            split_line[0] == "tags"
            or split_line[0] == "images"
            # or split_line[0] == "files" # not sure if files ever comes in as a list
        ):
            tags = convert_str_list_to_list(split_line[1])
            workshop_dictionary[split_line[0]] = tags
            continue
        workshop_dictionary[split_line[0]] = split_line[1]

    return workshop_dictionary


def grab_content(content: list[str], workshop_dictionary: dict) -> dict:
    for element in content:
        # IF IT'S A HEADING
        if element.startswith("#"):
            current_heading = element.strip("# ").strip()
            # Prepare a string to dump the rest of the content
            workshop_dictionary[current_heading] = ""
        # Assuming there is a heading to go off of
        elif current_heading:
            # HTML formatting line break
            if element == "":
                element = " <br> "
            workshop_dictionary[current_heading] += element
    return workshop_dictionary


def construct_workshop_dictionary(
    markdown_list: list[str], metadata: list[str], content: list[str]
) -> dict:
    workshop_dictionary = {}
    workshop_dictionary = grab_metadata(metadata, workshop_dictionary)
    workshop_dictionary = grab_content(content, workshop_dictionary)
    return workshop_dictionary


def load_markdown(markdown_file_path):
    """From a markdown file, load all information into a
    dictionary for the generator
    """
    with open(markdown_file_path, "r", encoding="utf-8") as file:
        markdown_text = file.read()
    markdown_list = markdown_text.split("\n")

    metadata = []
    content_index = 0
    for line in markdown_list:
        # CONTENT HAS STARTED
        if line.startswith("#"):
            break
        # Else append to metadata
        metadata.append(line)
        content_index += 1

    workshop_dictionary = construct_workshop_dictionary(
        markdown_list, metadata, markdown_list[content_index:]
    )
    # pprint(workshop_dictionary)
    return workshop_dictionary


def gen_tags(tags) -> str:
    first = """
    <div class = "tag-box">
        <p class = "tag">"""
    second = """</p>
    </div>
    """

    tags_str = ""
    for tag in tags:
        tags_str += first + tag + second

    return tags_str


def gen_img_strip(img_path_list) -> str:
    first = '<img class = "strip-photo" src="'
    second = '" alt="">\n'  # NOTE: can add alt text options here

    img_str = ""
    for img in img_path_list:
        img_str += first + img + second

    return img_str


def gen_workshop_page(workshop_dict: dict):
    download_html = "../downloads/float_boatGuide.pdf"
    workshop_title = workshop_dict["title"]

    description = workshop_dict["Description"]
    materials_and_preparation = workshop_dict["Materials"]

    tag_list = workshop_dict["tags"]
    tags_html = gen_tags(tag_list)

    img_path_list = workshop_dict["images"]
    # img_path_list = [
    #     "../img/float_boat/floatboat1.jpg",
    #     "../img/float_boat/floatboat2.jpg",
    #     "../img/float_boat/floatboat3.jpg",
    #     "../img/float_boat/floatboat4.jpg",
    # ]
    #
    images_html = gen_img_strip(img_path_list)

    workshop_page = f"""<!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="../css/ext/bootstrap.min.css">
            <link rel="stylesheet" href="../css/stylesheet.css">

            <title>Olin K12 Workshops</title>
        </head>

        <body>

            <nav class="fixed-top navbar navbar-expand-lg navbar-dark">
                <div class="container">
                    <a class="navbar-brand" href="index.html">
                        <img src="../img/olin_black.png" alt="Logo">
                    </a>
                    <span class="navbar-brand">K12 Workshops</span>
                    <button class="navbar-toggler hidden-sm-up float-xs-right" type="button" data-toggle="collapse"
                        data-target="#navcollapser" aria-controls="navcollapser" aria-expanded="false"
                        aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse justify-content-end" id="navcollapser">
                        <ul class="nav navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link active" href="../index.html">Gallery</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../about.html">About</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="https://www.olin.edu">Olin</a>
                            </li>
                            <!-- UNCOMMENT WHEN ARCHIVE IS WORKING -->
                            <!-- <li class="nav-item">
                                <a class="nav-link" href="archive.html">Archive</a>
                            </li> -->
                        </ul>
                    </div>
                </div>
            </nav>

        <!-- CHANGE TITLE and TAGS HERE-->

            <div class = "top-blurb container-fluid">
                <h2> {workshop_title}
                </h2>
                <div class = "row">
                    {tags_html}
                </div>
                
                </div>

            <div class = "meredith-workshop-content container-fluid">
                <div class = "row">
                    <div class = "col-lg-8">
                    <h2>Description</h2>
                    <p> 
                        {description}                   
                    </p>

                    <h2>Materials + Preparation</h2>
                    <p> 
                        {materials_and_preparation}
                </p>
                            
            
                
                </div>
                <div class = "col-lg-4">
                    <div class = "download-box img-holder"> <a href="{download_html}">
                        <p style = 'color: #ffffff'> Teacher's Guide 
                            <img id="download" style = "filter: invert(100%)" src="../assets/download.png">
                        </p> 
                    </a> </div>
                        
                    {images_html}

                    <!-- CHANGE SIDE PICS
                        HERE-->

                </div>
        </div>
        </div>
                
        </body>

        <script src="../js/ext/jquery-3.5.1.min.js"></script>
        <script src="../js/ext/bootstrap.bundle.min.js"></script>
        <script src="../js/script.js"></script>

        </html>
        """

    return workshop_page


if __name__ == "__main__":
    workshop_dict = load_markdown("markdowns/floatboats.md")
    pprint(workshop_dict)
    # tags = gen_tags(["E4E", "6-12", "smile"])

    # # print(tags)
    # img_path_list = ["../img/float_boat/floatboat1.jpg", "../img/float_boat/floatboat2.jpg", "../img/float_boat/floatboat3.jpg", "../img/float_boat/floatboat4.jpg"]
    # images_html = gen_img_strip(img_path_list)
    # print(images_html)
    out = gen_workshop_page(workshop_dict)
    with open("new_workshop.txt", "w") as file:
        file.write(out)
