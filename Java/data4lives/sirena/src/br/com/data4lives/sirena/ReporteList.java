public class ReporteList {

    private Reporte[] listaReportes;

    public ReporteList(int tamanho) {
        this.listaReportes = new Reporte[tamanho];
    }

    public Reporte[] getReportes() {
        return listaReportes;
    }
    public void setReportes(Reporte[] reportes) {
        this.listaReportes = reportes;
    }
    public void addReporte(Reporte reporte) {
        Reporte[] lista = new Reporte[listaReportes.length];
        for (int indiceReporte = 0; indiceReporte < listaReportes.length; indiceReporte++) {
            lista[indiceReporte] = listaReportes[indiceReporte];
        }
        lista[lista.length - 1] = reporte;
        listaReportes = lista;
    }

    public void grauConfiabilidade(Reporte[] lista, Confiabilidade confiabilidade) {
        for (int indiceReporte = 0; indiceReporte < lista.length; indiceReporte++) {
            int contadorReportes = 0;
            int idLocalizacao = lista[indiceReporte].getLocalizacao().getIdLocalizacao();
            String tipoReporte = lista[indiceReporte].getTipoReporte();
            for (int reporte = 0; reporte < lista.length; reporte++) {
                if (lista[reporte].getLocalizacao().getIdLocalizacao() == idLocalizacao && lista[reporte].getTipoReporte().equals(tipoReporte)) {
                    contadorReportes++;
                }
            }

            if (contadorReportes <= 3) {
                lista[indiceReporte].getConfiabilidade().setGrauConfiabilidade("Baixa");
            }
            else if (contadorReportes <= 9) {
                lista[indiceReporte].getConfiabilidade().setGrauConfiabilidade("Média");
            } else {
                lista[indiceReporte].getConfiabilidade().setGrauConfiabilidade("Alta");
            }
        }
    }
}
