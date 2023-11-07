def load_markdown():
    pass


def gen_tags(tags) -> str:
    first = '''
    <div class = "tag-box">
        <p class = "tag">'''
    second = '''</p>
    </div>
    '''
    
    tags_str = ""
    for tag in tags:
        tags_str += (first + tag + second)
        
    return tags_str

def gen_img_strip(img_path_list) -> str:
    first = '<img class = "strip-photo" src="'
    second = '" alt="">\n' # NOTE: can add alt text options here 
    
    img_str = ""
    for img in img_path_list:
        img_str += (first + img + second)
        
    return img_str

def gen_workshop_page():
    download_html = "../downloads/float_boatGuide.pdf"
    workshop_title = "To Float a Boat"
    
    description = '''
        Would your students have fun learning about buoyancy by
        getting their hands wet with some fun challenges? 
        This workshop will help students learn how boats work
        through a series of activities that cover buoyancy 
        and sail design through iterative building and hands-on group work. 
        Over the course of this workshop, students will build their own 
        cardboard boat from scratch and see how much “treasure” it can hold!
        <br>
        <br>
        Several of the described activities can take place concurrently, allowing students to choose with which stations
        they engage. A culminating large cardboard boat building activity can be contracted or 
        expanded as time allows.'''
    
    materials_and_preparation=f'''The <a href="{download_html}">Teacher's Guide </a> provides set-up instructions 
                    for multiple boat-related hands-on activites.
                    Most of the activities use common materials such as duct tape, tin foil, plastic bins, and discarded cardboard. 
                    One of the activities uses 3D-printed 
                    shapes as a way to explore buoyancy, but lower-fi alternatives can be used to a similar effect.'''
    
    tag_list = ["E4E", "Science", "Engineering", "1 hour", "Elementary"]
    tags_html = gen_tags(tag_list)
    
    
    img_path_list = ["../img/float_boat/floatboat1.jpg", "../img/float_boat/floatboat2.jpg", "../img/float_boat/floatboat3.jpg", "../img/float_boat/floatboat4.jpg"]
    images_html = gen_img_strip(img_path_list)
    
    download_html = "../downloads/float_boatGuide.pdf"
    
    workshop_page = f'''<!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="../css/ext/bootstrap.min.css">
            <link rel="stylesheet" href="../css/stylesheet.css">

            <title>Olin K12 Workshops</title>
        </head>

        <body>

            <nav class="fixed-top navbar navbar-expand-lg">
                <div class='row container-fluid'>
                        <a class="navbar-brand" href="../index.html">
                            <img src="../img/olin_workshops_left.png" alt="Logo">
                        </a>
                        <ul class="nav navbar-nav navbar-right">
                            <li class="nav-item">
                                <a class="nav-link active" href="../index.html">Gallery</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="../about.html">About</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" target = "_blank" href="https://www.olin.edu">Olin ></a>
                            </li>
                        </ul>
                        </div>
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

        <script src="js/ext/jquery-3.5.1.min.js"></script>
        <script src="js/ext/bootstrap.bundle.min.js"></script>
        <script src="js/script.js"></script>

        </html>
        '''
    
    return workshop_page

if __name__ == "__main__":
    # tags = gen_tags(["E4E", "6-12", "smile"])
    
    # # print(tags)
    # img_path_list = ["../img/float_boat/floatboat1.jpg", "../img/float_boat/floatboat2.jpg", "../img/float_boat/floatboat3.jpg", "../img/float_boat/floatboat4.jpg"]
    # images_html = gen_img_strip(img_path_list)
    # print(images_html)
    out = gen_workshop_page()
    with open("new_workshop.txt", "w") as file:
            file.write(out)
  
