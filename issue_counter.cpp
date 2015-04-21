#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;

char * input_file = "group4.txt";
int issue_position[100];

typedef struct
{
	string name;
	int times;
} name;

name namecount[8];

void getUsers(int start, int stop)
{
	string names[8];

	FILE * fp = fopen(input_file, "rb");
	fseek(fp, 0, SEEK_END);
	int file_size = ftell(fp);
	int name_count = 0;

	char * find_name = (char * )malloc(sizeof(char) * 30);
	for(int i = start; i < stop; i++)
	{
		fseek(fp, i, SEEK_SET);
		fread(find_name, sizeof(char), 30, fp);
		if(find_name[0] == 'u' && find_name[1] == 's' && find_name[2] == 'e' && find_name[3] == 'r')    //find issue position
		{
			char * get_name = (char *)malloc(sizeof(char) * 25);
			int j = 0;
			for(j; ((find_name[j + 7] != ',') && (find_name[j + 7] != '\n')); j++)
			{
				get_name[j] = find_name[j + 7];
			}
			get_name[j] = '\0';

			bool same = false;      // diff->false, same->true

			for(int k = 0; k < name_count; k++)
			{
				if(names[k] == get_name)
				{
					same = true;
				}
			}

			if((name_count == 0) || same == false)     //repeat
			{
				names[name_count] = get_name;
				name_count ++;
			}
		}
	}
	for(int i1 = 0; names[i1] != "\0"; i1++)
	{
		for(int i2 = 0; i2 < 8; i2++)
		{
			if(names[i1] == namecount[i2].name)
			{
				namecount[i2].times++;
				break;
			}
			else if(namecount[i2].times == 0)
			{
				namecount[i2].name = names[i1];
				namecount[i2].times++;
				break;
			}
		}
	}
	fclose(fp);
}

void findIDs()
{
	FILE * myfile = fopen( input_file, "rb" );
	fseek(myfile, 0, SEEK_END);
	int file_size = ftell(myfile);
	char * buffer = (char *)malloc(sizeof(char) * 5);
	int count = 0;   // num of issues
	int name = 0;    //user names
	for(int i = 0; i < file_size - 5; i++)
	{
		fseek(myfile, i, SEEK_SET);
		fread(buffer, sizeof(char), 5, myfile);
		if(buffer[0] == 'I' && buffer[1] == 'S' && buffer[2] == 'S' && buffer[3] == 'U' && buffer[4] == 'E')    //find issue position
		{
			issue_position[count] = ftell(myfile);
			count ++;       //num of ISSUE
		}
	}
	cout << "Number of issues: " << count << endl;
	for(int j = 0; j < count - 1; j++)
	{
		getUsers(issue_position[j], issue_position[j+1]);
	}
	getUsers(issue_position[count - 1], file_size);

	int i = 0;
}

void main()
{
	findIDs();

	for(int i = 0; namecount[i].times != 0; i++)
	{
		cout << namecount[i].name << " " << namecount[i].times << endl;
	}
}