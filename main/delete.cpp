#include <stdio.h>
#include <dirent.h>

int main()
{

    DIR *bad_moods = opendir("briank/shitty_thoughts");
    struct dirent *next_file;
    char filepath[256];

    while ( (next_file = readdir(bad_moods)) != NULL )
    {
        sprintf(filepath, "%s/%s", "briank/shitty_thoughts", next_file->d_name);
        remove(filepath);
    }
    closedir(bad_moods);
    return 0;
}