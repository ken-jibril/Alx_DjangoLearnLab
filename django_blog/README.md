# Django Blog — Tagging and Search Features

## Tagging

**Adding Tags to Posts:**  
- When creating or editing a post, use the **Tags** field to add multiple tags.  
- Tags are separated by commas.  
- Example: `Python, Django, WebDev`  

**Viewing Posts by Tag:**  
- Tags appear as clickable links on the post detail page.  
- Clicking a tag shows a list of all posts associated with that tag.  
- URL structure:  

- Example: clicking on the tag `django` leads to `/tags/django/`, displaying all posts tagged with Django.  

**Notes:**  
- Tags are case-insensitive and unique.  
- If a new tag does not exist in the database, it is created automatically when you save the post.  

---

## Search

**Using the Search Bar:**  
- The search bar is located in the **navigation header** for easy access.  
- Users can search for posts based on:  
- Title  
- Content keywords  
- Tag names  

**Search URL:**  


**Search Results:**  
- Displays a list of posts matching the search criteria.  
- Example: typing `django` will show all posts that contain the word “django” in the title, content, or tags.  
- If no posts match, a message **“No posts found.”** is displayed.  

---

## Testing Guidelines (Step 6)

1. **Tagging:**  
   - Create a post with multiple tags.  
   - Verify that tags appear correctly in post details.  
   - Click each tag and confirm the correct filtered list of posts appears.  

2. **Search:**  
   - Test searches using titles, content, and tags.  
   - Confirm results are accurate and the search bar redirects correctly.  
   - Test empty searches and keywords with no matching posts.  

3. **Permissions:**  
   - Only logged-in users can create/edit posts and comments.  
   - Viewing posts, tags, and search results works for all users.  

---

## Notes

- Tagging uses the **`django-taggit`** package for easy management.  
- Search functionality uses Django **Q objects** for filtering multiple fields.  
- These features are fully integrated with the existing blog system, maintaining a seamless user experience.  
