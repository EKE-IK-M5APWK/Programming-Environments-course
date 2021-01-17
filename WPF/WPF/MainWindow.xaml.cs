using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using WPF.Model;
using WPF.View;

namespace WPF
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public Shelter ShelterDatabase;
        public MainWindow()
        {
            
            InitializeComponent();
            ShelterDatabase = new Shelter();
            ShelterDatabase.Animals = readFromJson();
            lvAnimalList.ItemsSource = ShelterDatabase.Animals;
        }

        private void GetAnimalData(object sender, MouseButtonEventArgs e)
        {
            if (lvAnimalList.SelectedItem != null)
            {
                getAnimalDataView view = new getAnimalDataView()
                {
                    Animal = (Animal)lvAnimalList.SelectedItem
                };
                view.Show();
            }
        }

        private void NewAnimalClick(object sender, RoutedEventArgs e) 
        {
            newAnimalView animalView = new newAnimalView();
            bool dialogResult = (bool)animalView.ShowDialog();
            if(dialogResult){
                ShelterDatabase.Animals.Add(animalView.newAnimal);
                AddObjectsToJson(animalView.newAnimal);
                lvAnimalList.Items.Refresh();
                MessageBox.Show("Sikeres felvélte!","Állat Felvéltel",MessageBoxButton.OK,MessageBoxImage.Information);
            }
        }

        private void exitClick(object sender, RoutedEventArgs e)
        {
            System.Windows.Application.Current.Shutdown();
        }

        private List<Animal> readFromJson()
        {
             using (StreamReader r = new StreamReader(AppDomain.CurrentDomain.BaseDirectory + @"\database.json"))
             {
                    string json = r.ReadToEnd();
                    if (json.Length == 0)
                    {
                        return new List<Animal>();
                    }
                    var items = JsonConvert.DeserializeObject<List<Animal>>(json);
                    return items;
             }
  
        }
       public void AddObjectsToJson(Animal animal)
       {
           var initialJson = File.ReadAllText(AppDomain.CurrentDomain.BaseDirectory +@"\database.json");
           var array = JArray.Parse(initialJson);
           var itemToAdd = new JObject();
           itemToAdd["Name"] = animal.Name;
           itemToAdd["Age"] = animal.Age;
           itemToAdd["Species"] = animal.Species;
           itemToAdd["Breed"] = animal.Breed;
           itemToAdd["Color"] = animal.Color;
           itemToAdd["Weight"] = animal.Weight;
           itemToAdd["Height"] = animal.Height;
           itemToAdd["Sex"] = animal.Sex == Sex.Male ? 0 : 1;
           if (animal.Condition == StateOfCondition.Well)
           {
               itemToAdd["Condition"] = 0;
           }
           else if (animal.Condition == StateOfCondition.Sick)
           {
                itemToAdd["Condition"] = 1;
           }
           else
           {
                itemToAdd["Condition"] = 2;
           }

           itemToAdd["Adopted"] = animal.Adopted == Adopted.Igen ? 0 : 1;
           array.Add(itemToAdd);
           var jsonToOutput = JsonConvert.SerializeObject(array, Formatting.Indented);
           File.WriteAllText(AppDomain.CurrentDomain.BaseDirectory +@"\database.json",jsonToOutput);
       }
        
    }
}
