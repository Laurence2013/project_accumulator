Feature: Getting matches on a daily bases across all football competitions across the world according to Coral's website

Scenario: Admin clicks on update dates link, and selenium gets new daily match dates in the website

  Given that the web driver method is called and calling Firefox object
  When returning the chosen web link for Coral
  Then selenium will go to the link and grab the new daily match dates
