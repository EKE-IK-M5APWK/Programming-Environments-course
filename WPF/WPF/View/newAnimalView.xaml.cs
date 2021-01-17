using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using Newtonsoft.Json;
using WPF.Model;

namespace WPF.View
{
    /// <summary>
    /// Interaction logic for newAnimalView.xaml
    /// </summary>
    public partial class newAnimalView : Window
    {
        public Animal newAnimal { get; set; }
        public List<Sex> Sex { get; set; }
        public List<StateOfCondition> Conditions {get; set;}
        public List<Adopted> Adopted { get; set; }

        public string Path { get; set; }

        public newAnimalView()
        {
            InitializeComponent();
            ClassInitialize();
        }

        private void addNewAnimal(object sender, RoutedEventArgs e)
        {
            DialogResult = true;
        }

        private void Exit(object sender, RoutedEventArgs e)
        {
            DialogResult = false;
        }

        private void ClassInitialize()
        {

            newAnimal = new Animal();
            Sex = new List<Sex>() {Model.Sex.Male, Model.Sex.Female};
            Conditions = new List<StateOfCondition>()
                {StateOfCondition.Well, StateOfCondition.Sick, StateOfCondition.Rehabilitation};
            Adopted = new List<Adopted>() {Model.Adopted.Igen, Model.Adopted.Nem};
            this.DataContext = this;

        }

        private void TextBox_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            var textBox = sender as TextBox;
            e.Handled = Regex.IsMatch(e.Text, "[^0-9.]+");
        }
    }
}
