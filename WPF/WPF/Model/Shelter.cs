using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Windows.Documents;


namespace WPF.Model
{
    public class Shelter
    {
        public List<Animal> Animals { get; set; } = new List<Animal>();
    }

}
