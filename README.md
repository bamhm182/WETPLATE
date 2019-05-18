# WETPLATE

Wilson's Easy Tool for the Proficient Learning of All These Entities (WETPLATE) is a quick python script I made to help learn Military Wings, Groups, and Squadrons because it turns out that stuff isn't super easy to remember.

# Usage

There is an example_orgs.json file in this repository that gives you a template to work off of.
I didn't want to include any actual information because even though all the information is out there
on the internet, it still feels a little sensitive.

1) Copy example_orgs.json to orgs.json and add your entities.
2) Run gui.py after orgs.json is in the same folder. (Alternatively, I compiled a WETPLATE.exe
on the releases page. You can run that without Python.)

If you don't have an orgs.json file, it will automatically use example_orgs.json, so you can test it before putting
all your entities into a json.

# Entities

Entities have the following attributes:

Name: Name of the Entity  
Mission: What their official mission statement is  
Key Words: What they do in fewer words
Location: Where they are based  
Children: Array of entities they are over

They are written in the json as follows:

```json
{
  "orgs": [
      {
        "name": "Top Level Entity",
        "mission": "To accomplish top level stuff",
        "key_words": "Top Level Stuff",
        "location": "Anywhere and Everywhere",
        "children": [
          {
            "name": "Subordinate Entity",
            "mission": "To do subordinate stuff",
            "key_words": "Subordinate Stuff",
            "location": "Just Anywhere, not Everywhere",
            "children": [
              {
                "name": "Teensy Entity",
                "mission": "To finish teensy stuff",
                "key_words": "Teensy stuff",
                "location": "Everywhere, but not Anywhere"
              }
            ]
          }
        ]
      }
  ]
}
```

# Resizing
In theory, you could put as many entities and children as you need to, but it might look bad. It is programmed to
automatically space them based on the number of entities, but it might start to look pretty bad if you have a ton.

If you need more entities than the default resolution allows for, you can change it by editing gui.py and changing the
geometry from "1000x520" and the default width for draw_org() from 1000 to whatever you need.